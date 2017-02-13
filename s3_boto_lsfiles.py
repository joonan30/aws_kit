import boto

# s3 connection using boto
conn = boto.connect_s3()
bucket = conn.get_bucket('bucket_name')

# get the list of files on s3 using boto
items = bucket.list(prefix='folder_dir') # dir_dir/dir_dir/good_good
s3_files = []
for item in items:
	f_s3 = item.name.encode('utf-8').split('/')[-1]
	if 'gz' in f_s3:
		s3_files.append(f_s3)
	else:
		pass
