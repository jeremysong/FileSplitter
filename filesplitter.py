
def split(input_filename, output_prefix, output_suffix='data'):
    """
    Splits input file. It will throw StopIteration exception if the input file is not completed. For example,
    you may claim it has 5000 atoms at one TIMESTEP, but actually it only has less than 5000 atoms. However,
    this will not affect the results.

    :param input_filename: file name of input file. Pass complete path if this file is under different directory.
    :type input_filename: str or unicode
    :param output_prefix: prefix of output filename. Include path if those file are supposed to be written to a
                          different directory.
    :type output_prefix: str or unicode
    :param output_suffix: suffix(extension) of output filename without '.'. Default is data.
    :type output_suffix: str or unicode
    """
    output_id = 0
    input_file = open(input_filename, 'r')
    for line in input_file:
        if line.startswith('ITEM: TIMESTEP'):
            split_output_file = open(output_prefix + '_' + str(output_id) + '.' + output_suffix, 'w')
            split_output_file.write(line)

            num_atoms = 0
            for line_num in range(0, 8):
                if line_num == 2:
                    num_atom_line = next(input_file)
                    split_output_file.write(num_atom_line)
                    num_atoms = int(num_atom_line.strip())
                else:   
                    split_output_file.write(next(input_file))

            for _ in xrange(0, num_atoms):
                split_output_file.write(next(input_file))

            split_output_file.close()

            # Increment output file id
            output_id += 1

    input_file.close()

if __name__ == '__main__':
    split('PVP_Insert.lammpstrj', '/tmp/split')
    print("Program exits.")
