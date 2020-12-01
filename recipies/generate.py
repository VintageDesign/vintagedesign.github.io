#!/usr/bin/env python
import os
import markdown2

def main():
    with open('index.html', 'w+') as output_file:
        out_string = ""
        for filename in os.listdir(os.path.join(os.getcwd(), 'food')):
            with open(os.path.join(os.getcwd() + '/food' , filename), 'r') as input_file:
                print("Generating recipe for:", filename)
                out_string += markdown2.markdown(input_file.read())

        output_file.write(out_string)


if __name__ == "__main__":
    main()
