# cht-couchdb2googlepubsub
this software calls to couchdb/_changes feed once, in the api call it retrieves a BATCH_SIZE number of doc
data_records, and they are dispatched to pub/sub topics depending on year

Every 30 minutes this container is run, and each run has a maximum duration of 20 mins
With these settings we are treating about 960 000 docs by day

places and persons are dispatched to different pub/sub topics

For each pub/sub topic a bigquery table is subscribed to it, so json raw doc are automaticaly ingested to bigquery, this ingestion from pub/sub to BigQUery is managed by Google cLoud Platform

In BigQuery a suite of transformations is done 
