# State Legislator Ideologies

Publicized in the 2020.01.01 edition of Data is Plural newsletter.

> State legislator ideologies. Political scientists Boris Shor and Nolan McCarty’s have assigned ideology scores, on a conservative-to-liberal scale, to every US lawmaker in all 50 state legislatures. The most recent update, published May 2018, covers more than 22,000 legislators from 1993 through 2016. Shor and McCarty derived the numeric scores from a combination of legislative voting records and responses to Vote Smart’s “Political Courage Test.”

Project website: https://americanlegislatures.com/data/

Direct data source: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/BSLEFD

## Outcomes/Findings

1. Most of the data in this set is really boolean (e.g., `senate1993`) and is either `1.0` or `NaN`. The one numeric column that actually is numeric is the `np_score` column, though it is not clear from the data or directly in the codebook what that means and how to interpret it. (Yes, I could go look it up. The authors refernence a previously published paper that describes what the score means, but my goal was Pandas, not actually learning about the problem domain.)
2. This kind of descriptive analysis is really probably better suited for a Jupyter notebook, as most of what I was doing was done in an interactive python console.