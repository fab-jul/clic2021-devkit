# clic2021-devkit

Challenge homepage: [compression.cc](http://www.compression.cc).


## Downloading the Video challenge Data

To download all files, run:

```bash
bash download.sh path/to/data
```

It will create a folder `path/to/data` and extract all frames there, into a structure like:

```
video1/
    video1_frame1_y.png
    video1_frame1_u.png
    video1_frame1_v.png
    video1_frame2_y.png
    video1_frame2_u.png
    video1_frame2_v.png
    ...
video2/
    video2_frame1_y.png
    video2_frame1_u.png
    video2_frame1_v.png
    ...
```

For this, one of `gsutil`, `wget`, or `curl` must be available. `gsutil` is probably the most efficient way.

To download only some videos, use `--max_vides`: `bash download.sh path/to/data --max_videos 10`

**NOTE**: The script first downloads all vidoes as .zip files, resulting in 250GB+ of data.
Then all zips are decompressed one by one and subsequently deleted. If you interrupt the script
while unpacking, and later re-run it, it will re-download those that were already unpacked.
To prevent this at the expense of more hard-drive space used, you can keep the zip files by passing `--no_delete_zip`.

## Perceptual Challenge

This development kit is only provided as an example of what is expected from participants. It is in no way intended to contain data representative of the final challenge simply because that is not possible. The final test set will be created from the files uploaded by the participants in the compression challenge, and as a result it’s simply impossible for us to provide data which will match that distribution in the validation set.


You will first need to download the data from [here](https://storage.googleapis.com/clic2021_public/perceptual/clic_2021_perceptual_valid.zip). We recommend using `wget` to download this file as it supports
resuming the download gets interrupted.

The first step will be to unzip the data:

```bash
unzip clic_2021_perceptual_valid.zip
```

Once unzipped, this should contain 2730 PNG files. These are of the same size (768x768) that will be shown to human raters. The test set will be similarly distributed as PNG files. We don’t yet know how many there will be.

In addition to the PNG files, there are two important CSV files:

***validation.csv*** - this file is an example CSV file which contains the triplet PNG files that are used in the evaluation. The columns in this validation file are <O,A,B> (the file paths to the Original, A and B). The goal of your binary is to take this file as input, and generate a CSV file containing the same triplets, and an additional column which should contain either a 0, or a 1. The last column should have a 0 if the pair <O,A> will be preferred by humans to the pair <O,B>. Otherwise the last column should contain a 1. The output file format is the same as for oracle.csv, meaning we expect the columns to be <O,A,B,T> where T is the predicted value.

***oracle.csv*** - this file contains the “ground truth” and we provide it as a way to evaluate your metric by running “eval_csv.py”. This file will NOT be given to participants as part of the test set. The columns are <O,A,B,T> where T is the target value.


Here is a short description of the scripts related to the pereceptual challenge:

***eval_csv.py***: this script takes two arguments which are the oracle CSV (see below), and the CSV file generated by your metric.

Example usage:
```bash
# You only need to run this command once to install absl-py (a library that's used by eval_csv)
pip install absl-py

# Run this command as many times as you'd like
python3 eval_csv.py --oracle_csv oracle.csv --eval_csv psnr.csv
```

For convenience (and perhaps as a very naive starting point), we provide ***psnr.py*** which is a very simple script which can be used to produce outputs that are compatible with the evaluation script. This takes the validation.csv file (specified as an argument) and produces output compatible with eval_csv.py.

### 2022 Test Data (Released April 8th, 2022)

We've released the testing image files below. Please download them in order to produce the output from your algorithm.


The CSV file needed to compute binary decisions can be downloaded from:
  * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/clic2022_test.csv](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/clic2022_test.csv)
        Hash (md5):		942edd4ab592c196cf30b27e558bad66

The cropped images to be downloaded are as follows:
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/0.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/0.zip)
        Hash (md5):             b6eddbed2e88bfe20c101862a48e9f6c
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/1.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/1.zip)
        Hash (md5):             ce7a5e67fe069860dee965a015380eed
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/2.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/2.zip)
        Hash (md5):             cd8a305287bcf9b953f57bf982064be8
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/3.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/3.zip)
        Hash (md5):             9de2367d274b38d04bf846ed5257d7c0
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/4.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/4.zip)
        Hash (md5):             95eadd87afbf5034dc86010b977d29f5
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/5.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/5.zip)
        Hash (md5):             55af0df91e6bb8fe7f3e70ed4d37b497
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/6.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/6.zip)
        Hash (md5):             5e45727275e6d78ab6ec3ac28bbf62ed
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/7.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/7.zip)
        Hash (md5):             96db3240eabfeeb90f007564a5a68dcd
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/8.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/8.zip)
        Hash (md5):             bc7efed7f27d4d0649b6d4d6604dd74b
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/9.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/9.zip)
        Hash (md5):             e081e2eece15b352d1b90c6b5d2aa6dd
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/a.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/a.zip)
        Hash (md5):             69432ac41277b9dc30a02af78064c47e
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/b.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/b.zip)
        Hash (md5):             b404bcaf3fd1cdda3025cc9a5881cc39
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/c.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/c.zip)
        Hash (md5):             dd8d331c795913ec6ed940cb6c8e002c
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/d.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/d.zip)
        Hash (md5):             380d2c38410dd5152ec6f3940c453ed6
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/e.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/e.zip)
        Hash (md5):             1e15862bb4fb4d93fe647d32b3a2f25f
   * [https://storage.googleapis.com/clic2022_public/test_sets/perceptual/f.zip](https://storage.googleapis.com/clic2022_public/test_sets/perceptual/f.zip)
        Hash (md5):             271edee5431a82c6831cb20b0a46c921



### 2021 Test Data (Updated on January 20th, 2022, with the release of the oracle)

We released the following files which contain **768x768** (mostly - some files are slightly smaller in dimensions) crops:

* the test file (CSV) is [clic_2021_test.zip](https://storage.googleapis.com/clic2021_public/perceptual/test/clic_2021_test.zip). See "validation.csv" above for the details. This has the same format.
* the crop files, all of which need to be downloaded:
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/0.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/0.tar) MD5 (0.tar) = 1051e8adc4763c7f43a8bdde4007b08a
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/1.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/1.tar) MD5 (1.tar) = 015822694e53692cf6c9c68f6186ee1a
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/2.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/2.tar) MD5 (2.tar) = 76bf1c66114f882d040b3bc1ef07bb9a
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/3.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/3.tar) MD5 (3.tar) = 5dcd38f56982bc231156f63c2c7de97f
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/4.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/4.tar) MD5 (4.tar) = 09c6c620157fdf08e23c0d905af4536d
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/5.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/5.tar) MD5 (5.tar) = f6ba7d89dd69de00d71d86a8f02a9538
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/6.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/6.tar) MD5 (6.tar) = faf4e522548b0e6370bfc868e2e404c8
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/7.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/7.tar) MD5 (7.tar) = 8593b89231c0418a69f89c6187e0202a
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/8.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/8.tar) MD5 (8.tar) = 9d369a0b10ee923815b49b3c27726eee
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/9.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/9.tar) MD5 (9.tar) = 30876781abcd554939125490f8dc28a4
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/a.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/a.tar) MD5 (a.tar) = 5164040b4acd707575084968b0f94808
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/b.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/b.tar) MD5 (b.tar) = 34bc20563534730265dc26de12a29764
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/c.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/c.tar) MD5 (c.tar) = a3e8238bc5300d969e3b7421b0306bf6
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/d.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/d.tar) MD5 (d.tar) = 503dca354a62b9edd477c9b35d3afdf7
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/e.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/e.tar) MD5 (e.tar) = 1d5da08c1eb8f26463fd7c80e0be920b
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/f.tar](https://storage.googleapis.com/clic2021_public/perceptual/test/f.tar) MD5 (f.tar) = 3425385b344c5daf4bd7a3e526ff07a7

You could use the following snippet to download the files in parallel:

```bash
wget https://storage.googleapis.com/clic2021_public/perceptual/test/clic_2021_test.zip
for i in 0 1 2 3 4 5 6 7 8 9 a b c d e f; do
 # Note: remove the ampersand if you don't want to have 16 wget processes running at once
 wget https://storage.googleapis.com/clic2021_public/perceptual/test/$i.tar &
done
```

Once you've downloaded all the files, you'll need to unarchive them. 

```bash
unzip clic_2021_test.zip
for i in *.tar; do tar -xvf $i; done
```
This should yield the CSV file that you'll use to produce the results. The file paths are all relative to the directory where you unarchived everything.

### Ground Truth (Oracle Released: January 20th, 2022)

The oracle file (i.e., the file you can use to verify the performance of your algorithm/train new algorithms with this data) has been released. Please download it with the link below:
   * [https://storage.googleapis.com/clic2021_public/perceptual/test/clic_2021_perceptual_oracle.zip](https://storage.googleapis.com/clic2021_public/perceptual/test/clic_2021_perceptual_oracle.zip) MD5 (clic_2021_perceptual_oracle.zip) = c8f73bb863dfed677fe897dade35c89a

The oracle file is unfiltered, which means that any data cleanup is up to you. We left it like this on purpose, in order to allow participants to better model the human uncerntainty. We would like to highlight the fact that there is noise in this data, and therefore it's possible that a triplet might appear multiple times with both a positive and a negative label. 

If there's enough interest, we could be convinced to release an updated oracle which matches the cleanup methods we employed before using the data for the final scoring of CLIC 2021.

### Submitting to the validation/test server

Please follow our official submission form at [http://compression.cc/submit/](http://compression.cc/submit/). Choose the "Perceptual" task. You will need to provide the CSV file your algorithm has generated.

To view the current leaderboard, please go to [http://compression.cc/leaderboard/perceptual/valid/](http://compression.cc/leaderboard/perceptual/valid/). 
