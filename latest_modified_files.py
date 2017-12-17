def latest_modified_files(mod_within_days=0):
	import os,datetime, re
	src_dir = re.findall(r"[A-Z]+:.*$",os.popen("mountvol /").read(),re.MULTILINE)
	today =datetime.datetime.now()
	for src in src_dir:
		for dirpath, dirname, filename in os.walk(src):
	   		for fname in filename:
	   			if fname.endswith(".py"):
	   				path  = os.path.join(dirpath, fname)
	   				mtime = datetime.datetime.fromtimestamp(os.stat(path).st_mtime)
	   				ctime = datetime.datetime.fromtimestamp(os.stat(path).st_ctime)
	   				diff  = (today - mtime)
	   				days  = diff.days
	   				if days < mod_within_days:
	   					print('file:{0:15s} days:{1:2d} modified time:{2:10s} created time:{3:10s}'.format(fname,days,str(mtime),str(ctime)))

latest_modified_files(1)
	   