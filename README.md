# cht-couchdb2googlepubsub
this software calls to couchdb/_changes feed in a infinite loop successively, in each api call it retrieves a BATCH_SIZE number of doc
data_records are dispatched to pub/sub topics depending on year

places and persons are dispatched to different pub/sub topics

For each pub/sub topic a bigquery table is subscribed to it, so json raw doc are automaticaly ingested to bigquery, this ingestion from pub/sub to BigQUery is managed by Google cLoud Platform

In BigQuery a suite of transformations is done
