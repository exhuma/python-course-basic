def main():
    with open('data_latin1.csv', encoding='latin1') as infile1:
        data_1 = infile1.readlines()
    with open('data_utf8.csv', encoding='utf8') as infile2:
        data_2 = infile2.readlines()

    all_lines_a = set(data_1)
    all_lines_b = set(data_2)
    
    only_in_a = all_lines_a - all_lines_b
    only_in_b = all_lines_b - all_lines_a
    in_both_files = all_lines_a & all_lines_b

    print('Only in Latin-1 file:')
    for row in only_in_a:
        print(row.strip())

    print('Only in UTF-8 file:')
    for row in only_in_b:
        print(row.strip())

    print('Lines in both files:')
    for row in in_both_files:
        print(row.strip())


main()
