% Run: problog 04_problog.pl
0.8::rain.
0.6::sprinkler.
wet_grass :- rain.
wet_grass :- sprinkler.
query(wet_grass).
