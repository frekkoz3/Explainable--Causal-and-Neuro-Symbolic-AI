% Run: problog 05_problog_evidence.pl
0.2::disease.
0.9::positive_test :- disease.
0.1::positive_test :- \+disease.
evidence(positive_test,true).
query(disease).
