#!/usr/bin/bash
echo '####################################'
echo 'Creating Tables ...'
echo '####################################'
echo ''
psql -d um2024_db -a -f data/schema.sql
echo ''
echo '####################################'
echo 'Tables Created successfully'
echo '####################################'
echo ''
echo '####################################'
echo 'Inserting Values into Tables...'
echo '####################################'
cat data/inventory.csv | psql -U um2024 -d um2024_db -c "COPY inventory from STDIN CSV HEADER"
cat data/wine.csv | psql -U um2024 -d um2024_db -c "COPY wine from STDIN CSV HEADER"
cat data/charcuterie.csv | psql -U um2024 -d um2024_db -c "COPY charcuterie from STDIN CSV HEADER"
cat data/orders.csv | psql -U um2024 -d um2024_db -c "COPY orders from STDIN CSV HEADER"
cat data/region.csv | psql -U um2024 -d um2024_db -c "COPY region from STDIN CSV HEADER"
cat data/owner.csv | psql -U um2024 -d um2024_db -c "COPY owner from STDIN CSV HEADER"
cat data/contents.csv | psql -U um2024 -d um2024_db -c "COPY contents from STDIN CSV HEADER"
cat data/stocked.csv | psql -U um2024 -d um2024_db -c "COPY stocked from STDIN CSV HEADER"
cat data/consists.csv | psql -U um2024 -d um2024_db -c "COPY consists from STDIN CSV HEADER"
cat data/winery_owns.csv | psql -U um2024 -d um2024_db -c "COPY winery_owns from STDIN CSV HEADER"
cat data/make.csv | psql -U um2024 -d um2024_db -c "COPY make from STDIN CSV HEADER"
cat data/account_has.csv | psql -U um2024 -d um2024_db -c "COPY account_has from STDIN CSV HEADER"
cat data/customer_belong.csv | psql -U um2024 -d um2024_db -c "COPY customer_belong from STDIN CSV HEADER"
cat data/place.csv | psql -U um2024 -d um2024_db -c "COPY place from STDIN CSV HEADER"
echo '####################################'
echo 'Values Inserted Successfully'
echo '####################################'
