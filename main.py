#Thanks for support with this poject to the following:
#Hunter College's Professor Zamansky
#Victoria for sharing the Python script that creates tables from CSVs in a SQLite 3 database and then allows queries to be run
#The Flask Mega-Tutorial (Parts 1-4) (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)
#The Replit Flask Tutorial (https://replit.com/talk/learn/Flask-Tutorial-Part-1-the-basics/26272)
#Stack Overflow (stackoverflow.com)

import random, string, pandas as pd, sqlite3
from flask import Flask, render_template, redirect, url_for, request, session



app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.secret_key="something"

ok_chars = string.ascii_letters + string.digits

@app.route('/')  # What happens when the user visits the site
def base_page():
  if 'name' not in session:
    session['name']=''
  random_num = random.randint(1, 100000)  # Sets the random number
  return render_template(
		'base.html',  # Template file path, starting from the templates folder. 
		random_number=random_num , username=session['name'] 
    # Sets the variable random_number in the template
	)


@app.route('/aboutUs.html')
def aboutUs():
  
  rand_ammnt = random.randint(10, 100)
  random_str = random.randint(1, 100000) 
  if 'name' not in session:
    session['name']=''
  return render_template('aboutUs.html', random_number=random_str, username=session['name'] )

@app.route('/scan.html') # Initialize the database
def scan():
  if 'name' not in session:
   session['name']=''
  rand_ammnt = random.randint(10, 100)
  random_str = random.randint(1, 100000) 
  sql_query_string = """
    SELECT * 
    FROM scan
  """

  def sql_query_to_pd(sql_query_string: str, db_name: str ='default.db') -> pd.DataFrame:  
  # Step 1: Connect to the SQL DB
    con = sqlite3.connect(db_name)

  # Step 2: Execute the SQL query
    cursor = con.execute(sql_query_string)

  # Step 3: Fetch the data and column names
    result_data = cursor.fetchall()
    cols = [description[0] for description in cursor.description]

  # Step 4: Close the connection
    con.close()

  # Step 5: Return as a dataframe
    return pd.DataFrame(result_data, columns=cols)
  
#Exectue the SQL query
  result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
  result_df
  return render_template('scan.html', tables=[result_df.to_html(classes='data')], titles=result_df.columns.values, username=session['name'] )

@app.route('/bio.html') # Initialize the database
def bio():
  if 'name' not in session:
    session['name']=''
  rand_ammnt = random.randint(10, 100)
  random_str = random.randint(1, 100000) 
  sql_query_string = """
    SELECT * 
    FROM bio
  """

  def sql_query_to_pd(sql_query_string: str, db_name: str ='default.db') -> pd.DataFrame:  
  # Step 1: Connect to the SQL DB
    con = sqlite3.connect(db_name)

  # Step 2: Execute the SQL query
    cursor = con.execute(sql_query_string)

  # Step 3: Fetch the data and column names
    result_data = cursor.fetchall()
    cols = [description[0] for description in cursor.description]

  # Step 4: Close the connection
    con.close()

  # Step 5: Return as a dataframe
    return pd.DataFrame(result_data, columns=cols)
  
#Exectue the SQL query
  result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
  result_df
  return render_template('bio.html', tables=[result_df.to_html(classes='data')], titles=result_df.columns.values, username=session['name'] )

@app.route('/periodAttendance.html') # Initialize the database
def periodAttendance():
  if 'name' not in session:
    session['name']=''
  rand_ammnt = random.randint(10, 100)
  random_str = random.randint(1, 100000) 
  sql_query_string = """
    SELECT * 
    FROM periodAtt
  """

  def sql_query_to_pd(sql_query_string: str, db_name: str ='default.db') -> pd.DataFrame:  
  # Step 1: Connect to the SQL DB
    con = sqlite3.connect(db_name)

  # Step 2: Execute the SQL query
    cursor = con.execute(sql_query_string)

  # Step 3: Fetch the data and column names
    result_data = cursor.fetchall()
    cols = [description[0] for description in cursor.description]

  # Step 4: Close the connection
    con.close()

  # Step 5: Return as a dataframe
    return pd.DataFrame(result_data, columns=cols)
  
#Exectue the SQL query
  result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
  result_df
  return render_template('periodAttendance.html', tables=[result_df.to_html(classes='data')], titles=result_df.columns.values, username=session['name'] )

@app.route('/cuts.html') # Initialize the database
def cuts():
  if 'name' not in session:
    session['name']=''
  rand_ammnt = random.randint(10, 100)
  random_str = random.randint(1, 100000) 
  sql_query_string = """
    SELECT p.First, p.Last, p.StudentID, p.Grade, ScanTime, Status, Date, CourseSection, Attendance, Teacher, Period
FROM scan AS s
INNER JOIN periodAtt AS p
ON s.StudentID=p.StudentID AND substr(ScanTime, 1,inStr(ScanTime, ' ')-1)=p.Date
WHERE Attendance='A'
ORDER BY p.Last, p.First
  """

  def sql_query_to_pd(sql_query_string: str, db_name: str ='default.db') -> pd.DataFrame:  
  # Step 1: Connect to the SQL DB
    con = sqlite3.connect(db_name)

  # Step 2: Execute the SQL query
    cursor = con.execute(sql_query_string)

  # Step 3: Fetch the data and column names
    result_data = cursor.fetchall()
    cols = [description[0] for description in cursor.description]

  # Step 4: Close the connection
    con.close()

  # Step 5: Return as a dataframe
    return pd.DataFrame(result_data, columns=cols)
  
#Exectue the SQL query
  result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
  result_df
  return render_template('cuts.html', tables=[result_df.to_html(classes='data')], titles=result_df.columns.values, username=session['name'] )

@app.route('/cutsBySection.html') # Initialize the database
def cutsBySection():
  if 'name' not in session:
    session['name']=''
  rand_ammnt = random.randint(10, 100)
  random_str = random.randint(1, 100000) 
  sql_query_string = """
  SELECT * FROM
(
SELECT courseSection, teacher, COUNT(*) AS totalCuts
FROM
(
SELECT *
FROM scan AS s
INNER JOIN periodAtt AS p
ON s.StudentID=p.StudentID AND substr(ScanTime, 1,inStr(ScanTime, ' ')-1)=p.Date
WHERE Attendance='A'
) AS allCuts
GROUP BY courseSection
HAVING substr(courseSection,1,1)='M'
) AS myTable2
WHERE teacher IN ('Siena, V', 'Jarding, T', 'Rael, S', 'Oto, T', 'Klar, S', 'Pylant, C')
ORDER BY totalCuts DESC
  """

  def sql_query_to_pd(sql_query_string: str, db_name: str ='default.db') -> pd.DataFrame:  
  # Step 1: Connect to the SQL DB
    con = sqlite3.connect(db_name)

  # Step 2: Execute the SQL query
    cursor = con.execute(sql_query_string)

  # Step 3: Fetch the data and column names
    result_data = cursor.fetchall()
    cols = [description[0] for description in cursor.description]

  # Step 4: Close the connection
    con.close()

  # Step 5: Return as a dataframe
    return pd.DataFrame(result_data, columns=cols)
  
#Exectue the SQL query
  result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
  result_df
  return render_template('cutsBySection.html', tables=[result_df.to_html(classes='data')], titles=result_df.columns.values, username=session['name'] )


@app.route('/cutsByTeacher.html') # Initialize the database
def cutsByTeacher():
  if 'name' not in session:
    session['name']=''
  rand_ammnt = random.randint(10, 100)
  random_str = random.randint(1, 100000) 
  sql_query_string = """
   SELECT Teacher, COUNT(*) AS Total
FROM
(
SELECT *
FROM scan AS s
INNER JOIN periodAtt AS p
ON s.StudentID=p.StudentID AND substr(ScanTime, 1,inStr(ScanTime, ' ')-1)=p.Date
WHERE Attendance='A'
) AS allCuts
GROUP BY Teacher
ORDER BY Total DESC
  """

  def sql_query_to_pd(sql_query_string: str, db_name: str ='default.db') -> pd.DataFrame:  
  # Step 1: Connect to the SQL DB
    con = sqlite3.connect(db_name)

  # Step 2: Execute the SQL query
    cursor = con.execute(sql_query_string)

  # Step 3: Fetch the data and column names
    result_data = cursor.fetchall()
    cols = [description[0] for description in cursor.description]

  # Step 4: Close the connection
    con.close()

  # Step 5: Return as a dataframe
    return pd.DataFrame(result_data, columns=cols)
  
#Exectue the SQL query
  result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
  result_df
  return render_template('cutsByTeacher.html', tables=[result_df.to_html(classes='data')], titles=result_df.columns.values, username=session['name'] )

@app.route('/cutsByPeriod.html') # Initialize the database
def cutsByPeriod():
  if 'name' not in session:
    session['name']=''
  rand_ammnt = random.randint(10, 100)
  random_str = random.randint(1, 100000) 
  sql_query_string = """
   SELECT First, Last, StudentID, SUM (Pd1) AS Pd1_, SUM (Pd2) AS Pd2_, SUM (Pd3) AS Pd3_, SUM (Pd4) AS Pd4_, SUM (Pd5) AS Pd5_, SUM (Pd6) AS Pd6_, SUM (Pd7) AS Pd7_, SUM (Pd8) AS Pd8_, SUM (Pd9) AS Pd9_, 
SUM (PD1)+SUM(PD2)+SUM(PD3)+SUM(PD4)+SUM(PD5)+SUM(PD6)+SUM(PD7)+SUM(PD8)+SUM(PD9) as Total
FROM
(
SELECT First, Last, StudentID, 
(Period=1) AS Pd1,
(Period=2) AS Pd2,
(Period=3) AS Pd3,
(Period=4) AS Pd4,
(Period=5) AS Pd5,
(Period=6) AS Pd6,
(Period=7) AS Pd7,
(Period=8) AS Pd8,
(Period=9) AS Pd9
FROM
(
SELECT *
FROM scan AS s
INNER JOIN periodAtt AS p
ON s.StudentID=p.StudentID AND substr(ScanTime, 1,inStr(ScanTime, ' ')-1)=p.Date
WHERE Attendance='A'
)

)
GROUP BY StudentID, Last, First
ORDER BY Last, First


  """

  def sql_query_to_pd(sql_query_string: str, db_name: str ='default.db') -> pd.DataFrame:  
  # Step 1: Connect to the SQL DB
    con = sqlite3.connect(db_name)

  # Step 2: Execute the SQL query
    cursor = con.execute(sql_query_string)

  # Step 3: Fetch the data and column names
    result_data = cursor.fetchall()
    cols = [description[0] for description in cursor.description]

  # Step 4: Close the connection
    con.close()

  # Step 5: Return as a dataframe
    return pd.DataFrame(result_data, columns=cols)
  
#Exectue the SQL query
  result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
  result_df
  return render_template('cutsByPeriod.html', tables=[result_df.to_html(classes='data')], titles=result_df.columns.values, username=session['name'] )

@app.route('/cutsWithBio.html') # Initialize the database
def cutsWithBio():
  if 'name' not in session:
    session['name']=''
  rand_ammnt = random.randint(10, 100)
  random_str = random.randint(1, 100000) 
  sql_query_string = """
   SELECT b.First, b.Last, b.StudentID, Grade,ScanTime, Status, Date, CourseSection, Attendance, Teacher, Period, Parent1Phone, Parent2Phone, ParentEmail
FROM
(
SELECT *
FROM scan AS s
INNER JOIN periodAtt AS p
ON s.StudentID=p.StudentID AND substr(ScanTime, 1,inStr(ScanTime, ' ')-1)=p.Date
WHERE Attendance='A'
) AS allCuts
LEFT JOIN bio AS b
ON allCuts.StudentID=b.StudentID
  """

  def sql_query_to_pd(sql_query_string: str, db_name: str ='default.db') -> pd.DataFrame:  
  # Step 1: Connect to the SQL DB
    con = sqlite3.connect(db_name)

  # Step 2: Execute the SQL query
    cursor = con.execute(sql_query_string)

  # Step 3: Fetch the data and column names
    result_data = cursor.fetchall()
    cols = [description[0] for description in cursor.description]

  # Step 4: Close the connection
    con.close()

  # Step 5: Return as a dataframe
    return pd.DataFrame(result_data, columns=cols)
  
#Exectue the SQL query
  result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
  result_df
  return render_template('cutsWithBio.html', tables=[result_df.to_html(classes='data')], titles=result_df.columns.values, username=session['name'] )


@app.route("/form_demo.html",methods=['GET','POST'])
def form_demo():
  if 'name' not in session:
    session['name']=''
     # GET is when we just load the page in our browser
  # POST is when we click the button 
  if request.method=="GET":
    return render_template("form_demo.html")
  else:
    # here we clicked the button
    # so we can check the form data
    name = request.form['username']
    pw = request.form['password']
    favoriteQuery=request.form['favoriteQuery']
    session['name'] = request.form.get('username')
    session['pw'] = request.form.get('pw')
    session['favoriteQuery'] = request.form.get('favoriteQuery')
    print(name,pw)
    error = ""
    if pw == "":
      error = "Please enter a valid username and password."
      name=""
      pw=""
    if name == "":
      error = "Please enter a valid username and password."
      name=""
      pw=""
    return render_template("form_demo.html",error=error, name=name, favoriteQuery=favoriteQuery, username=session['name'] )

@app.route('/initialize.html') # Initialize the database
def initializeMyDB():
  if 'name' not in session:
    session['name']=''
  rand_ammnt = random.randint(10, 100)
  random_str = random.randint(1, 100000) 
  return render_template('initialize.html', random_number=random_str)
  
#start database code
  def pd_to_sqlDB(input_df: pd.DataFrame,
                table_name: str,
                db_name: str = 'default.db') -> None:
     # Step 1: Setup local logging
    import logging
    logging.basicConfig(level=logging.INFO,
                       format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

   # Step 2: Find columns in the dataframe
    cols = input_df.columns
    cols_string = ','.join(cols)
    val_wildcard_string = ','.join(['?'] * len(cols))

    # Step 3: Connect to a DB file if it exists, else crete a new file
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    logging.info(f'SQL DB {db_name} created')

    # Step 4: Create Table
    sql_string = f"""CREATE TABLE {table_name} ({cols_string});"""
    cur.execute(sql_string)
    logging.info(f'SQL Table {table_name} created with {len(cols)} columns')

    # Step 5: Upload the dataframe
    rows_to_upload = input_df.to_dict(orient='split')['data']
    sql_string = f"""INSERT INTO {table_name} ({cols_string}) VALUES ({val_wildcard_string});"""
    cur.executemany(sql_string, rows_to_upload)
    logging.info(f'{len(rows_to_upload)} rows uploaded to {table_name}')
  
    # Step 6: Commit the changes and close the connection
    con.commit()
    con.close()


  def sql_query_to_pd(sql_query_string: str, db_name: str ='default.db') -> pd.DataFrame:  
  # Step 1: Connect to the SQL DB
    con = sqlite3.connect(db_name)

  # Step 2: Execute the SQL query
    cursor = con.execute(sql_query_string)

  # Step 3: Fetch the data and column names
    result_data = cursor.fetchall()
    cols = [description[0] for description in cursor.description]

  # Step 4: Close the connection
    con.close()

  # Step 5: Return as a dataframe
    return pd.DataFrame(result_data, columns=cols)

  #Bio TABLE
# Step 1: Read the csv file into a dataframe
  input_df = pd.read_csv('attendanceTables/bio.csv')
 
# Step 2: Upload the dataframe to a SQL Table
  pd_to_sqlDB(input_df,
            table_name='Bio',
            db_name='default.db')

#Scan TABLE
# Step 1: Read the csv file into a dataframe
  input_df = pd.read_csv('attendanceTables/scanTimes.csv')
 
# Step 2: Upload the dataframe to a SQL Table
  pd_to_sqlDB(input_df,
            table_name='Scan',
            db_name='default.db')

#Period Attendance TABLE
# Step 1: Read the csv file into a dataframe
  input_df = pd.read_csv('attendanceTables/periodAttendance.csv')
 
# Step 2: Upload the dataframe to a SQL Table
  pd_to_sqlDB(input_df,
            table_name='periodAtt',
            db_name='default.db')

#end database code

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)