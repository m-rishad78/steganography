from PIL import Image
from os import path
from argparse import ArgumentParser

from collections.abc import Generator
from typing import Any

class Steganography:
    def __init__(self) -> None:
        try:
            self.parser: ArgumentParser= ArgumentParser()
            self.parser.add_argument(
                '-m',
                '--mode',
                type=str,
                help="[e - Encoding | d - Decoding]",
                required=True
            )
            self.parser.add_argument(
                '-f',
                '--file',
                type=str,
                help='Input filename',
                required=True
            )
            self.parser.add_argument(
                '-d',
                '--data',
                type=str,
                help='Data to be encoded'
            )
            self.parser.add_argument(
                '-o',
                '--out',
                type=str,
                help='Output filename'
            )
            self.args= self.parser.parse_args()
        except Exception as e:
            print(f'Error: {str(e)}')

    def modify_pixels(self, pixels: list[tuple[int]], data: str) -> Generator[tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]], None, None]:
        try:
            data_list: list[str]= [format(ord(i), '08b') for i in data]
            len_data: int= len(data_list)
            img_data: iter= iter(pixels)

            for i in range(len_data):
                block: list[int]= list(
                    next(img_data)[:3] +
                    next(img_data)[:3] +
                    next(img_data)[:3]
                )

                for j in range(8):
                    if data_list[i][j] == '0' and block[j] % 2 != 0:
                        block[j]-= 1

                    elif data_list[i][j] == '1' and block[j] % 2 == 0:
                        block[j]= block[j]+1 if block[j] == 0 else block[j]-1 

                else:
                    if i == len_data - 1:
                        if block[-1] % 2 == 0:
                            block[-1]= block[-1]+1 if block[-1] == 0 else block[-1]-1

                    else:
                        if block[-1] % 2 != 0:
                            block[-1]-= 1

                block= tuple(block)

                yield block[0:3], block[3:6], block[6:9]

        except Exception as e:
            print(f'Error: {str(e)}')

    def encode_data(self, img_obj: Image.Image, data: str) -> None:
        try:
            x= y= 0
            w= img_obj.size[0]

            for p1, p2, p3 in self.modify_pixels(pixels=img_obj.getdata(), data=data):
                img_obj.putpixel((x, y), p1)
                x, y= (0, y+1) if x == w-1 else (x+1, y)

                img_obj.putpixel((x, y), p2)
                x, y= (0, y+1) if x == w-1 else (x+1, y)

                img_obj.putpixel((x, y), p3)
                x, y= (0, y+1) if x == w-1 else (x+1, y)

        except Exception as e:
            print(f'Error: {str(e)}')

    def encode(self, in_file: str, data: str, out_file: str) -> None:
        try:
            img_obj: Image.Image= Image.open(fp=in_file).copy()
            w, h= img_obj.size
            capacity: int= (w * h) // 3

            if len(data) > capacity:
                raise ValueError("Data is too large for this image!")

            self.encode_data(img_obj=img_obj, data=data)
            img_obj.save(fp=out_file)
            img_obj.close()

        except Exception as e:
            print(f'Error: {str(e)}')

    def decode(self, in_file: str) -> None:
        try:
            img: Image.Image= Image.open(fp=in_file).copy()
            img_data: iter= iter(img.getdata())

            data: str= ''

            while True:
                block: list[int]= list(
                    next(img_data)[:3] +
                    next(img_data)[:3] +
                    next(img_data)[:3]
                )

                bin_str: str= ''.join('0' if i % 2 == 0 else '1' for i in block[:8])
                data+= chr(int(bin_str, 2))

                if block[-1] % 2 != 0:
                    break

            print(data)

        except StopIteration:
            print('Error: Reached end of image without finding terminator bit!')

        except Exception as e:
            print(f'Error: {str(e)}')

    def main(self) -> None:
        try:
            mode: str= self.args.mode.strip().lower()
            in_file: str= self.args.file.strip()
            data: str | None= self.args.data if self.args.data else None
            out_file: str | None= self.args.out if self.args.out else None

            if not path.exists(in_file):
                raise ValueError("File not found!")

            match (mode):
                case 'e':
                    if data is None:
                        raise ValueError("No data provided for encoding!")

                    if out_file is None:
                        raise ValueError("Output file (-o) is required for encoding!")
                    
                    self.encode(in_file=in_file, data=data, out_file=out_file)

                case 'd':
                    self.decode(in_file=in_file)

                case _:
                    print("\nInvalid option.")

        except Exception as e:
            print(f'Error: {str(e)}')


if __name__ == '__main__':
    sg: Steganography= Steganography()
    sg.main()