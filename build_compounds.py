#!/usr/bin/env python3
"""
2018-02-27 whikloj
Builds Islandora compound image flat file structure from multiple images and a single MODS record.
"""
import argparse
import re
import os
import shutil

multiple_images = re.compile('^([\w\-_]+?)([0-9]+)\.(\w{3,4})$')


def gather_all_files(directory):
    new_files = [f for topDir, dirs, files in os.walk(directory) for f in files]
    return new_files


def map_image_to_metadata(image_files, metadata_files):
    maps = [(i, os.path.splitext(i)[0] + '.mods') for i in image_files if os.path.splitext(i)[0] + '.mods' in metadata_files ]
    return maps


def count_collection(image_files):
    files_directory = {}
    for i in image_files:
        if multiple_images.search(i):
            matches = multiple_images.match(i)
            try:
                files_directory[matches.group(1)] += 1
            except KeyError:
                files_directory[matches.group(1)] = 1
    return files_directory


def main(args):
    image_files = gather_all_files(args.image_directory)
    mods_files = gather_all_files(args.mods_directory)
    file_dict = map_image_to_metadata(image_files, mods_files)
    compound_count = count_collection(image_files)
    for (image, meta) in file_dict:
        if multiple_images.search(image):
            matches = multiple_images.match(image)
            new_dir = matches.group(1)
            sequence_number = matches.group(2)
            obj_ext = matches.group(3)
        else:
            (new_dir, obj_ext) = os.path.splitext(image)
            sequence_number = "1"
        new_dir = new_dir.lower().replace(' ', '_').replace('-', '_')
        if compound_count[matches.group(1)] > 1:
            type_dir = os.path.join(args.output_dir, 'compounds')
            object_dir = os.path.join(type_dir, new_dir)
            output = os.path.join(object_dir, sequence_number)
        else:
            type_dir = os.path.join(args.output_dir, 'large_images')
            output = os.path.join(type_dir, new_dir)
        build_dir(output, args.output_dir)
        copy_file(
            os.path.join(args.image_directory, image),
            os.path.join(output, 'OBJ.' + obj_ext)
        )
        copy_file(
            os.path.join(args.mods_directory, meta),
            os.path.join(output, 'MODS.xml')
        )
        if compound_count[matches.group(1)] > 1 and int(sequence_number) == 1:
            # Also copy this MODS to the compound level
            copy_file(
                os.path.join(args.mods_directory, meta),
                os.path.join(object_dir, 'MODS.xml')
            )


def build_dir(final_dir, top_dir):
    if not os.path.exists(final_dir) and os.path.realpath(final_dir) != os.path.realpath(top_dir):
        build_dir(os.path.dirname(final_dir), top_dir)
        os.mkdir(final_dir, 0o775)


def copy_file(copy_from, copy_to):
    if not os.path.exists(copy_to) or args.overwrite:
        shutil.copyfile(
            copy_from,
            copy_to
        )
        log_copy(
            copy_from,
            copy_to
        )
    else:
        log_skip(
            copy_to
        )


def log(message):
    print(message)


def log_copy(copy_from, copy_to):
    # We aren't writing to a log
    log("Copied {} -> {}".format(copy_from, copy_to))


def log_skip(copy_to):
    log("Skip overwriting {}".format(copy_to))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Copy multiple files from separate image and metadate directories in' +
                                                 ' to a flat structure for batch compounding.')
    parser.add_argument('--images', dest='image_directory', required=True, help='Directory of images to copy')
    parser.add_argument('--metadata', dest='mods_directory', required=True, help='Directory of metadata files, with ' +
                                                                                 'same basename as images')
    parser.add_argument('--output', dest='output_dir', required=True, help='Directory to build compounds under')
    parser.add_argument('-w', '--overwrite', dest="overwrite", action="store_true", default=False,
                        help="Overwrite existing files.")
    args = parser.parse_args()

    # Make absolute.
    if args.image_directory[0] != '/':
        args.image_directory = os.path.realpath(os.path.join(os.getcwd(), args.image_directory))
    if args.mods_directory[0] != '/':
        args.mods_directory = os.path.realpath(os.path.join(os.getcwd(), args.mods_directory))
    if args.output_dir[0] != '/':
        args.output_dir = os.path.realpath(os.path.join(os.getcwd(), args.output_dir))
    for i in [args.image_directory, args.mods_directory, args.output_dir]:
        if not os.path.exists(i) or not os.path.isdir(i) or not os.access(i, os.R_OK):
            parser.error("Directory ({}) does not exist, or is not readable".format(i))
    if not os.access(args.output_dir, os.W_OK):
        parser.error("Output directory ({}) is not writable.".format(args.output_dir))
    main(args)
