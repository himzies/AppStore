# Construct the URI from the .env
DB_HOST='ec2-3-212-45-192.compute-1.amazonaws.com'
DB_NAME='d3eubjpp8qsgok'
DB_USER='xnmwpcdoapzinc'
DB_PORT='5432'
DB_PASSWORD='83eeca0d8cc02131d26fcdeb6197b38988776ec765d35c182383144d0f8c6e0b'

while IFS= read -r line
do
  if [[ $line == DB_HOST* ]]
  then
    DB_HOST=$(cut -d "=" -f2- <<< $line | tr -d \')
  elif [[ $line == DB_NAME* ]]
  then
    DB_NAME=$(cut -d "=" -f2- <<< $line | tr -d \' )
  elif [[ $line == DB_USER* ]]
  then
    DB_USER=$(cut -d "=" -f2- <<< $line | tr -d \' )
  elif [[ $line == DB_PORT* ]]
  then
    DB_PORT=$(cut -d "=" -f2- <<< $line | tr -d \')
  elif [[ $line == DB_PASSWORD* ]]
  then
    DB_PASSWORD=$(cut -d "=" -f2- <<< $line | tr -d \')
  fi
done < ".env"

URI="postgres://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME"

# Run the scripts to insert data.
psql ${URI} -f sql/AlfredoClean.sql
psql ${URI} -f sql/AlfredoSchema.sql
psql ${URI} -f sql/AlfredoCustomers.sql
psql ${URI} -f sql/AlfredoProviders.sql
psql ${URI} -f sql/AlfredoJobs.sql
