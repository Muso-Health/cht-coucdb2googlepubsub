# cht-couchdb2googlepubsub
this software calls to couchdb/_changes feed once per container run, in this api call it retrieves a BATCH_SIZE number of docs,
from these docs, data_record are dispatched to pub/sub topics depending on year

places and persons are dispatched to different pub/sub topics

other docs are ignored

For each pub/sub topic a bigquery table is subscribed to it, so json raw doc are automatically ingested to bigquery, this ingestion from pub/sub to BigQuery is managed by Google cLoud Platform

In BigQuery a suite of transformations is done

the container is executed every 20 minutes, this timing is controlled by the Google cloud scheduler
the container have a maximum request duration of 19minutes this is 1140 seconds

with this we have an ingestion capacity of 120 000 docs by hour
