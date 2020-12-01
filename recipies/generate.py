#!/usr/bin/env python
import os
import markdown2

def main():
    with open('index.html', 'w+') as output_file:
        with open(os.path.join(os.getcwd(), 'base.html'), 'r') as input_file:
            out_string = input_file.read()
        for filename in sorted(os.listdir(os.path.join(os.getcwd(), 'food'))):
            if filename != "template.md":
                with open(os.path.join(os.getcwd() + '/food' , filename), 'r') as input_file:
                    print("Generating recipe for:", filename)
                    out_string += "<hr>"
                    out_string += markdown2.markdown(input_file.read())


        output_file.write(out_string)


if __name__ == "__main__":
    main()
