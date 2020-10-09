import git, os, shutil, stat, mariadb
import mysql.connector
import urllib.request

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False

def del_evenReadonly(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

# Get dir one level up
parent_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
target_dir = parent_dir + '\FlaskEwatsonTEST'
print(target_dir)

# We should test Internet before we delete
if(connect()):
        
    """
    # Remove old code
    print("Looking for target")
    if os.path.exists(target_dir):
        print("Removing")
        shutil.rmtree(target_dir,onerror=del_evenReadonly)

    # Get master branch
    print("Downloading")
    git.repo.base.Repo.clone_from('https://github.com/han-SDU/FlaskEwatson.git',target_dir)

    """
    # Set up db
    conn = mysql.connector.connect(
                user="root",
                password="1234",
                host="localhost"
            )
    cursor = conn.cursor()

    file = open(target_dir+'\sqlScript\dbCreation.sql')
    sql = file.read()
    for result in cursor.execute(sql, multi=True):
        if result.with_rows:
            print("Rows produced by statement '{}':".format(
                result.statement))
            print(result.fetchall())
        else:
            print("Number of rows affected by statement '{}': {}".format(
            result.statement, result.rowcount))
    conn.close()

print("Done")