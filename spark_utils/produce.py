from topics import Topic
listen = Topic('listen-events', 9092, '/Users/chris/pyprojects/Beatstream/spark_utils/new_parqs/streaming_events_5_12_24.parquet')
# analysis = Topic('analysis', 9092, '/Users/chris/Downloads/mill_songs/analysis copy.csv')
# tracks = Topic('tracks', 9092, '/Users/chris/Downloads/mill_songs/tracks copy.csv')

listen.p_produce()
# analysis.c_produce()
# tracks.c_produce()
