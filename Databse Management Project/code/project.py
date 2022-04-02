import streamlit as st
import pandas as pd
import psycopg2 as ps
from configparser import ConfigParser

st.set_page_config(layout="wide",initial_sidebar_state="auto")
@st.cache
def get_config(filename="database.ini", section="postgresql"):
	parser= ConfigParser()
	parser.read(filename)
	return {k: v for k, v in parser.items(section)}

@st.cache
def query_db(sql: str):
	db_info = get_config()
	conn = ps.connect(**db_info)
	cur = conn.cursor()
	cur.execute(sql)
	data = cur.fetchall()
	column_names = [desc[0] for desc in cur.description]
	conn.commit()
	cur.close()
	conn.close()
	df = pd.DataFrame(data=data, columns=column_names)
	return df

def main():
	menu = ["All Information","Top Customers","Check Bottle Count","Wine","Winery Managers","Charcuterie Board Options","Inventory","Recommendation Engine"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "All Information":
		head = st.container()
		with head:
			head_col1,head_col2 = st.columns((1,3))
			#st.markdown("<img src='images/wine-splash.jpg' style='float: center'>",unsafe_allow_html=True)
			with head_col1:
				st.image("images/wine-splash.jpg",width=250)
			with head_col2:
				st.markdown("<h1 style='text-align: center'>Wine-Splash Database Management Dashboard</h1>",unsafe_allow_html=True)
				st.markdown("<h3 style='text-align: center'>One Stop shop for all information</h3>",unsafe_allow_html=True)
		# Reading all the Tables
		"## Read from Database"
		sql_all_table_names = "SELECT relname FROM pg_class WHERE relkind='r' AND relname !~ '^(pg_|sql_)';"
		try:
		    all_table_names = query_db(sql_all_table_names)["relname"].tolist()
		    table_name = st.selectbox("Choose a table", all_table_names)
		except:
		    st.write("Sorry! Something went wrong with your query, please try again.")

		if table_name != 'account_has':
		    f"Here's the info"
		    sql_table = f"SELECT * FROM {table_name};"
		    try:
		    	df = query_db(sql_table)
		    	st.dataframe(df)
		    except:
		        st.write("Sorry! Something went wrong with your query, please try again.")

		elif table_name == 'account_has':
			f"Here is the partial info"
			f"Note: Some of the sensitive information cannot be displayed, contact manager"
			sql_table = f"SELECT name,username,dob,contact,email,license FROM {table_name};"
			try:
		        	df = query_db(sql_table)
		       		st.dataframe(df)
			except:
				st.write("Sorry! Something went wrong with your query, please try again.")

	elif choice == "Top Customers":
		head = st.container()
		with head:
			head_col1,head_col2 = st.columns((1,3))
			#st.markdown("<img src='images/wine-splash.jpg' style='float: center'>",unsafe_allow_html=True)
			with head_col1:
				st.image("images/wine-splash.jpg",width=250)
			with head_col2:
				st.markdown("<h1 style='text-align: center'>Wine-Splash Database Management Dashboard</h1>",unsafe_allow_html=True)
				st.markdown("<h3 style='text-align: center'>One Stop shop for all information</h3>",unsafe_allow_html=True)
		col1,col2= st.columns(2)
		with col1:
			"## Query the top customers"
			st.write("Here are customers that spent the most with us, just slide to select the count")
			try:
				l=[1,2,3,4,5,6,7,8,9,10]
				customer_count = st.select_slider("", options=l)
			except:
			    st.write("Sorry! Something went wrong with your query, please try again.")

			if customer_count == l[0]:
			    sql_customer = f"SELECT C.name AS customer_name,COUNT(*) AS number_of_orders,SUM(O.cost) AS Total_amount FROM customer_belong C, orders O, place P WHERE C.cid=P.cid AND O.orderid=P.orderid GROUP BY 1 HAVING COUNT(*) > 1 ORDER BY 3 DESC LIMIT {customer_count};"
			    try:
			    	df = query_db(sql_customer)
			    	st.dataframe(df)
			    except:
			        st.write(
			            "Sorry! Something went wrong with your query, please try again."
					)

			if customer_count == l[1]:
			    sql_customer = f"SELECT C.name AS customer_name,COUNT(*) AS number_of_orders,SUM(O.cost) AS Total_amount FROM customer_belong C, orders O, place P WHERE C.cid=P.cid AND O.orderid=P.orderid GROUP BY 1 HAVING COUNT(*) > 1 ORDER BY 3 DESC LIMIT {customer_count};"
			    try:
			    	df = query_db(sql_customer)
			    	st.dataframe(df)
			    except:
			        st.write(
			            "Sorry! Something went wrong with your query, please try again."
					)
			if customer_count == l[2]:
			    sql_customer = f"SELECT C.name AS customer_name,COUNT(*) AS number_of_orders,SUM(O.cost) AS Total_amount FROM customer_belong C, orders O, place P WHERE C.cid=P.cid AND O.orderid=P.orderid GROUP BY 1 HAVING COUNT(*) > 1 ORDER BY 3 DESC LIMIT {customer_count};"
			    try:
			    	df = query_db(sql_customer)
			    	st.dataframe(df)
			    except:
			        st.write(
			            "Sorry! Something went wrong with your query, please try again."
					)
			if customer_count == l[3]:
			    sql_customer = f"SELECT C.name AS customer_name,COUNT(*) AS number_of_orders ,SUM(O.cost) AS Total_amount FROM customer_belong C, orders O, place P WHERE C.cid=P.cid AND O.orderid=P.orderid GROUP BY 1 HAVING COUNT(*) > 1 ORDER BY 3 DESC LIMIT {customer_count};"
			    try:
			    	df = query_db(sql_customer)
			    	st.dataframe(df)
			    except:
			        st.write(
			            "Sorry! Something went wrong with your query, please try again."
					)
			if customer_count == l[4]:
				sql_customer = f"SELECT C.name AS customer_name,COUNT(*) AS number_of_orders,SUM(O.cost) AS Total_amount FROM customer_belong C, orders O, place P WHERE C.cid=P.cid AND O.orderid=P.orderid GROUP BY 1 HAVING COUNT(*) > 1 ORDER BY 3 DESC LIMIT {customer_count};"
				try:
					df = query_db(sql_customer)
					st.dataframe(df)
				except:
					st.write("Sorry! Something went wrong with your query, please try again."
					)
			if customer_count == l[5]:
				sql_customer = f"SELECT C.name AS customer_name,COUNT(*) AS number_of_orders,SUM(O.cost) AS Total_amount FROM customer_belong C, orders O, place P WHERE C.cid=P.cid AND O.orderid=P.orderid GROUP BY 1 HAVING COUNT(*) > 1 ORDER BY 3 DESC LIMIT {customer_count};"
				try:
					df = query_db(sql_customer)
					st.dataframe(df)
				except:
					st.write("Sorry! Something went wrong with your query, please try again."
					)
			if customer_count == l[6]:
				sql_customer = f"SELECT C.name AS customer_name,COUNT(*) AS number_of_orders,SUM(O.cost) AS Total_amount FROM customer_belong C, orders O, place P WHERE C.cid=P.cid AND O.orderid=P.orderid GROUP BY 1 HAVING COUNT(*) > 1 ORDER BY 3 DESC LIMIT {customer_count};"
				try:
					df = query_db(sql_customer)
					st.dataframe(df)
				except:
					st.write("Sorry! Something went wrong with your query, please try again."
					)
			if customer_count == l[7]:
				sql_customer = f"SELECT C.name AS customer_name,COUNT(*) AS number_of_orders,SUM(O.cost) AS Total_amount FROM customer_belong C, orders O, place P WHERE C.cid=P.cid AND O.orderid=P.orderid GROUP BY 1 HAVING COUNT(*) > 1 ORDER BY 3 DESC LIMIT {customer_count};"
				try:
					df = query_db(sql_customer)
					st.dataframe(df)
				except:
					st.write("Sorry! Something went wrong with your query, please try again."
					)
			if customer_count == l[8]:
				sql_customer = f"SELECT C.name AS customer_name,COUNT(*) AS number_of_orders,SUM(O.cost) AS Total_amount FROM customer_belong C, orders O, place P WHERE C.cid=P.cid AND O.orderid=P.orderid GROUP BY 1 HAVING COUNT(*) > 1 ORDER BY 3 DESC LIMIT {customer_count};"
				try:
					df = query_db(sql_customer)
					st.dataframe(df)
				except:
					st.write("Sorry! Something went wrong with your query, please try again."
					)
			if customer_count == l[9]:
				sql_customer = f"SELECT C.name AS customer_name,COUNT(*) AS number_of_orders,SUM(O.cost) AS Total_amount FROM customer_belong C, orders O, place P WHERE C.cid=P.cid AND O.orderid=P.orderid GROUP BY 1 HAVING COUNT(*) > 1 ORDER BY 3 DESC LIMIT {customer_count};"
				try:
					df = query_db(sql_customer)
					st.dataframe(df)
				except:
					st.write("Sorry! Something went wrong with your query, please try again."
					)
		with col2:
			"## Query each order"
			sql_order_ids = "SELECT orderid FROM orders;"
			try:
			    order_ids = query_db(sql_order_ids)["orderid"].tolist()
			    order_id = st.selectbox("Choose an order", order_ids)
			except:
			    st.write("Sorry! Something went wrong with your query, please try again.")

			if order_id:
				sql_order = f"SELECT C.name, O.odate, O.cost FROM orders as O, customer_belong as C, place as P WHERE O.orderid = '{order_id}' AND P.orderid = O.orderid AND P.cid = C.cid;"
				try:
					customer_info = query_db(sql_order).loc[0]
					customer_name, order_date, order_cost = (
						customer_info["name"],
						customer_info["odate"],
						customer_info["cost"],
						)
					st.write(f"This order was placed by {customer_name} on {order_date} and it's cost was ${order_cost}.")
					
				except:
					st.write(
			            "Sorry! Something went wrong with your query, please try again."
			        )

	elif choice == "Check Bottle Count":
		head = st.container()
		with head:
			head_col1,head_col2 = st.columns((1,3))
			#st.markdown("<img src='images/wine-splash.jpg' style='float: center'>",unsafe_allow_html=True)
			with head_col1:
				st.image("images/wine-splash.jpg",width=250)
			with head_col2:
				st.markdown("<h1 style='text-align: center'>Wine-Splash Database Management Dashboard</h1>",unsafe_allow_html=True)
				st.markdown("<h3 style='text-align: center'>One Stop shop for all information</h3>",unsafe_allow_html=True)

		"## Check Wine Bottle count by Alcohol%"
		try:
			x = st.number_input("Choose Alcohol Percentage",12,17)
		except:
			st.write("Sorry! Something went wrong with your query, please try again.")
			
		if x:
		    sql_alcohol = f"SELECT W.name, SUM(I.bottlecount) AS Total_Bottlecount FROM wine W, stocked S, inventory I WHERE W.wineid = S.wineid AND S.invid = I.invid AND W.alcohol_percentage = {x} GROUP BY 1 ORDER BY 2 DESC;"

		    try:
		        df = query_db(sql_alcohol)
		        st.dataframe(df)
		    except:
		        st.write(
		            "Sorry! Something went wrong with your query, please try again."
		        )	

	elif choice == "Wine":
		head = st.container()
		with head:
			head_col1,head_col2 = st.columns((1,3))
			#st.markdown("<img src='images/wine-splash.jpg' style='float: center'>",unsafe_allow_html=True)
			with head_col1:
				st.image("images/wine-splash.jpg",width=250)
			with head_col2:
				st.markdown("<h1 style='text-align: center'>Wine-Splash Database Management Dashboard</h1>",unsafe_allow_html=True)
				st.markdown("<h3 style='text-align: center'>One Stop shop for all information</h3>",unsafe_allow_html=True)






		"## Wine Info"
		sql_wine_types = "SELECT type FROM wine group by type;"
		try:
			l=['DESC','ASC']
			show = ['High to Low','Low to High']
			wine_types = query_db(sql_wine_types)["type"].tolist()
			wine_type = st.radio("Choose a Wine Type", wine_types)
			sort_type = st.radio("Sort by Price", show)
			show[0] = l[0]
			show[1] = l[1]
		except:
		    st.write("Please select a wine type")
		if wine_type:
			if l[0]:
				sql_wine = f"SELECT name,age,price FROM wine WHERE type = '{wine_type}' ORDER BY price {sort_type};"
				try:
					#The problem is it retruns only 1st value, not all
				    #wine_info = query_db(sql_wine).loc[0]
					df = query_db(sql_wine)
					st.dataframe(df)
				except:
					st.write(
						"Please select atleast a wine type"
					)
			else:
				sql_wine = f"SELECT name,age,price FROM wine WHERE type = '{wine_type}' ORDER BY price {sort_type};"
				try:
					#The problem is it retruns only 1st value, not all
				    #wine_info = query_db(sql_wine).loc[0]
					df = query_db(sql_wine)
					st.dataframe(df)
				except:
					st.write(
						"Please select atleast a wine type"
					)

	elif choice == "Winery Managers":
		head = st.container()
		with head:
			head_col1,head_col2 = st.columns((1,3))
			#st.markdown("<img src='images/wine-splash.jpg' style='float: center'>",unsafe_allow_html=True)
			with head_col1:
				st.image("images/wine-splash.jpg",width=250)
			with head_col2:
				st.markdown("<h1 style='text-align: center'>Wine-Splash Database Management Dashboard</h1>",unsafe_allow_html=True)
				st.markdown("<h3 style='text-align: center'>One Stop shop for all information</h3>",unsafe_allow_html=True)
		"## Manager Info"
				
		sql_region_ids = "SELECT country FROM region order by country;"
		try:
			region_types = query_db(sql_region_ids)["country"].tolist()
			region_type = st.selectbox("Select the region", region_types)
		except:
		    st.write("Sorry! Something went wrong with your query, please try again.")

		if region_type:
		    sql_region = f"SELECT A.name AS Manager,W.name AS Winery, O.contact FROM winery_owns W, owner O, account_has A, region R WHERE W.address = '{region_type}' AND W.name = O.winery AND O.owner_ssn = A.ssn GROUP BY 1,2,3;"
		    try:
		        manager_info = query_db(sql_region)
		        st.dataframe(manager_info)
		    except:
		        st.write(
		            "Sorry! Something went wrong with your query, please try again."
				)

	elif choice == "Charcuterie Board Options":
		head = st.container()
		with head:
			head_col1,head_col2 = st.columns((1,3))
			#st.markdown("<img src='images/wine-splash.jpg' style='float: center'>",unsafe_allow_html=True)
			with head_col1:
				st.image("images/wine-splash.jpg",width=250)
			with head_col2:
				st.markdown("<h1 style='text-align: center'>Wine-Splash Database Management Dashboard</h1>",unsafe_allow_html=True)
				st.markdown("<h3 style='text-align: center'>One Stop shop for all information</h3>",unsafe_allow_html=True)

		"## Charcuterie Board Options"
		board_col1,board_col2 = st.columns(2)

		#Category of Boards
		with board_col1:
			sql_board_options= "SELECT DISTINCT category FROM contents;"
			try:
				board_types = query_db(sql_board_options)["category"].tolist()
				board_type = st.multiselect("Select board category", board_types)
				#st.write("You selected - ", f'{board_type}')
				#st.write(type(board_type))
				# s = ","
				# s = s.join(board_type)
				s = ''
				for i in range(len(board_type)-1):
					s += "'"+board_type[i]+"'"+","
				s += "'"+board_type[len(board_type)-1]+"'"
				#st.write(s)

			except:
				st.write("Please select atleast 1 category")

			if board_type:
				board_sql = f"SELECT CB.boardid, CB.name,C.content FROM charcuterie AS CB, contents AS C WHERE C.boardid = CB.boardid AND C.category in ({s}) GROUP BY 1,2,3 ORDER BY 1,2,3;"
				try:
					board_info = query_db(board_sql)
					st.dataframe(board_info)
				except:
					st.write("Something Went Wrong")

	elif choice == "Inventory":
		head = st.container()
		with head:
			head_col1,head_col2 = st.columns((1,3))
			#st.markdown("<img src='images/wine-splash.jpg' style='float: center'>",unsafe_allow_html=True)
			with head_col1:
				st.image("images/wine-splash.jpg",width=250)
			with head_col2:
				st.markdown("<h1 style='text-align: center'>Wine-Splash Database Management Dashboard</h1>",unsafe_allow_html=True)
				st.markdown("<h3 style='text-align: center'>One Stop shop for all information</h3>",unsafe_allow_html=True)

		" ## Wine Status in Inventory "

		sql_inv_type = "SELECT DISTINCT type FROM inventory ORDER BY type;"
		try:
			inv_types = query_db(sql_inv_type)
			inv_type = st.selectbox("Select the Inventory Type",inv_types)
		except:
			st.write("Something Went Wrong")


		if inv_type:
			sql_inv_status = f"SELECT W.name AS Winename, W.popularity AS Percentage_Popularity, I.bottlecount AS Instock, (2021-W.age) AS wine_age FROM wine W, inventory I, stocked S WHERE I.type = '{inv_type}' AND I.invid = S.invid AND S.wineid = W.wineid ORDER BY 2 DESC,3 DESC;"
			try:
				inv_info = query_db(sql_inv_status)
				st.dataframe(inv_info)
			except:
				st.write("Something Went Wrong")

	elif choice == "Recommendation Engine":

		head = st.container()
		with head:
			head_col1,head_col2 = st.columns((1,3))
			#st.markdown("<img src='images/wine-splash.jpg' style='float: center'>",unsafe_allow_html=True)
			with head_col1:
				st.image("images/wine-splash.jpg",width=250)
			with head_col2:
				st.markdown("<h1 style='text-align: center'>Wine-Splash Database Management Dashboard</h1>",unsafe_allow_html=True)
				st.markdown("<h3 style='text-align: center'>One Stop shop for all information</h3>",unsafe_allow_html=True)


		button_col1,button_col2 = st.columns(2)
		with button_col1:
			"## The Most Popular Charcuterie Board"
			result = st.button("Click Here to get the Most Trending Charcuterie Board")

			if result:
				sql_board = f"SELECT CB.name, COUNT(*) FROM consists C, charcuterie CB WHERE CB.boardid = C.boardid and CB.boardid != 'CB_000' GROUP BY 1 ORDER BY 2 DESC LIMIT 1;"
				try:
					board_info = query_db(sql_board).loc[0]
					b_name, b_count = (
			        	board_info["name"],
			        	board_info["count"],
			        	)
					st.write(f"The Best Selling Charcuterie Board is {b_name} and the units sold were {b_count}")
						
				except:
					st.write(
						"Sorry! Something went wrong with your query, please try again. in 2"
						)
		with button_col2:
			"## The Most Popular Wine"
			result = st.button("Click Here to get the Most Trending Wine")

			if result:
				sql_board = f"SELECT W.name, COUNT(*)*18 FROM consists C, wine W WHERE W.wineid = C.wineid GROUP BY 1 ORDER BY 2 DESC LIMIT 1;"
				try:
					board_info = query_db(sql_board).loc[0]
					b_name, b_count = (
			        	board_info["name"],
			        	board_info["?column?"],
			        	)
					st.write(f"The Best Selling Wine is {b_name} and the units sold were {b_count}")
						
				except:
					st.write(
						"Sorry! Something went wrong with your query, please try again. in 2"
						)
if __name__ == '__main__':
	main()
