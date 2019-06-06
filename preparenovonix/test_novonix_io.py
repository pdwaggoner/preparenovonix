import os
import preparenovonix.novonix_variables as nv
import preparenovonix.novonix_io as prep

exfile = "example_data/example_data.csv"
exfile_prep = "example_data/example_data_prep.csv"


def test_get_infile():
    exprep = "example_data/example_data_prep_prep.csv"
    prep.get_infile(exfile_prep, overwrite=False)
    assert os.stat(exfile_prep).st_size == os.stat(exprep).st_size
    os.remove(exprep)


def test_isnovonix():
    assert prep.isnovonix(exfile) is True
    assert prep.isnovonix("novonix_add") is False


def test_icolumn():
    assert prep.icolumn(exfile_prep, nv.col_step) > -1
    assert prep.icolumn(exfile_prep, nv.col_tstep) > -1
    assert prep.icolumn(exfile_prep, "Random name") == -1


def test_read_column():
    col = prep.read_column(exfile_prep, nv.col_step, outtype="int")
    assert len(col) > 1
    assert min(col) > -1


def test_replace_file():
    longf = "test_l.txt"
    lf = open(longf, "w")
    lf.write("This is a longer file")
    lf.close()
    shortf = "test_s.txt"
    sf = open(shortf, "w")
    sf.write("Short file")
    sf.close()
    prep.replace_file(longf, shortf, newbigger=True)
    assert os.path.isfile(longf) is False
    os.remove(shortf)
