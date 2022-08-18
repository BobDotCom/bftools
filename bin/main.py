import argparse

import bftools

parser = argparse.ArgumentParser(description="bftools brainfuck toolbox")
parser.add_argument(
    "-v", "--verbose", help="verbose output (not implemented yet)", action="store_true"
)
parser.add_argument(
    "-V",
    "--version",
    help="show version",
    action="version",
    version=f"%(prog)s {bftools.__version__}",
)

subparsers = parser.add_subparsers(
    title="Commands",
    description="Commands for actually doing stuff",
    dest="command_type",
)

compile = subparsers.add_parser("compile", help="compile brainfuck into python")
compile.add_argument("input", help="code to compile")
decode = subparsers.add_parser("decode", help="decode brainfuck into text")
decode.add_argument("input", help="code to decode")
encode = subparsers.add_parser("encode", help="encode text into brainfuck")
encode.add_argument("input", help="text to encode")

args = parser.parse_args()

bf = bftools.BrainfuckTools()

if args.command_type == "compile":
    code = bf.compile(args.input).result
    parser.exit(message=code)
elif args.command_type == "decode":
    text = bf.decode(args.input).result
    parser.exit(message=text)
elif args.command_type == "encode":
    code = bf.encode(args.input).result
    parser.exit(message=code)
