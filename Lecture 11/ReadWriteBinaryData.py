import pickle


def main():

    outfile = open("pickle.dat", "wb")
    pickle.dump(45, outfile)
    pickle.dump(2.5, outfile)
    pickle.dump([1, 2, 3], outfile)
    pickle.dump((1, 2, 3, 5, 45), outfile)
    outfile.close()

    infile = open("pickle.dat", "rb")
    print(pickle.load(infile))
    infile.close()


main()