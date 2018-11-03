import os
import sys
import shutil
import tempfile
import glob

class MakePackage():
    @staticmethod
    def add_package(cdict):
        sys.exit(1) # not implemented
        package_name = cdict['package_name']
        shutil.copytree('templates', package_name)
        files = glob.glob('{0}/**'.format(package_name), recursive=True)
        files.extend(glob.glob('{0}/.**'.format(package_name), recursive=True))
        for f in files:
            print(f)
            # if os.path.isdir(f):
            #     if not os.path.exists(f):
            #         os.makedirs(f)
            # elif not os.path.exists(f):
            #     # shutil.copy(f)
            #     MakePackage.convert_file(f, cdict)

    @staticmethod
    def make_package(cdict):
        package_name = cdict['package_name']
        has_test = cdict['has_test'] == 'y'
        shutil.copytree('templates', package_name)
        os.rename('{}/package_folder'.format(package_name), '{0}/{0}'.format(package_name))
        os.rename('{0}/{0}/package.py'.format(package_name), '{0}/{0}/{0}.py'.format(package_name))
        if not has_test:
            shutil.rmtree('{0}/test'.format(package_name))
        files = glob.glob('{0}/**'.format(package_name), recursive=True)
        files.extend(glob.glob('{0}/.**'.format(package_name), recursive=True))
        for f in files:
            if os.path.isdir(f):
                continue
            MakePackage.convert_file(f, cdict)

    @staticmethod
    def convert_file(f, cdict):
        __, path = tempfile.mkstemp()
        with open(path,'w') as of:
            remove_if_section = None
            for line in open(f):
                skip = False # don't skip writing line
                if remove_if_section:
                    if r'<%%!endif_%s!%%>' %remove_if_section in line:
                        remove_if_section = None
                    continue

                for k,v in cdict.items():
                    if k == 'git_url' and f == 'testit/README.md':
                        print("----------",line)
                    line = line.replace(r'<%%!%s!%%>'%k,v)
                    if r'<%%!if_%s!%%>'%k in line and not v:
                        remove_if_section = k
                        skip = True
                if not skip:
                    of.write(line)
        os.rename(path, f)

def verify_arg(k,v):
    if not v:
        print('Argument"%s"is required'%k)
        sys.exit(1)

def cl_mk_package():
    """
    Command Line Make Package
    """
    cdict = {}
    cdict['package_name'] = input("package_name (lowercase): ")
    print(cdict['package_name'])
    if os.path.exists(cdict['package_name']):
        raise FileExistsError('The package "%s" already exists'%cdict['package_name'])
    for k,v in cdict.items():
        verify_arg(k,v)
    cdict['author'] = input("Author (or None): ")
    cdict['email'] = input("Email (or None): ")
    cdict['class_name'] = input("Class_Name (or None): ")
    cdict['version'] = input("version (1.0.0): ") or '1.0.0'
    cdict['description'] = input("description (or None): ")
    cdict['has_test'] = input("Test Directory [y/N]: ") or 'n'
    cdict['git_url'] = input("Git Url (or None): ") or ''
    cdict['console_scripts'] = ''
    cdict['install_requires'] = input("required installs (or None): ") or ''
    MakePackage.make_package(cdict)
