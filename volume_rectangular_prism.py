#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: June 2022
# This program gets the volume of a rectangular prism


def volume_of_cylinder(height, width, length):
    # calculate volume

    volume = width * height * length

    return volume


def main():
    # this function gets the height, width and length

    while True:
        try:
            # input
            height_as_float = float(
                input("Enter the height of the rectangular prism(mm): ")
            )
            width_as_float = float(
                input("Enter the width of the rectangular prism(mm): ")
            )
            length_as_float = float(
                input("Enter the length of the rectangular prism(mm): ")
            )
            # call functions
            calculated_volume = volume_of_cylinder(
                height_as_float, width_as_float, length_as_float
            )
            calculated_volume = round(calculated_volume, 2)
            print(
                "The volume of this rectangular prism with the width of {0} mm, height of {1} mm, and length of {2} mm is {3} mm³.".format(
                    width_as_float, height_as_float, length_as_float, calculated_volume
                )
            )
            break
        except Exception:
            print("That is not an float, try again.")
            continue
    print("\nDone.")


if __name__ == "__main__":
    main()
