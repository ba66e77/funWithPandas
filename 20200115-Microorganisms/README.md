# Microorganisms

Publicized in the 2020.01.15 edition of Data is Plural newsletter.

>  The Microbe Directory is an attempt to profile more than 7,000 bacteria, viruses, archaea, and other microorganisms. The directory can be downloaded in bulk and describes the microbes’ optimal temperature, optimal pH, Gram stain, pathogenicity, antimicrobial resistance, and more.

Project website: https://microbe.directory/

Direct data source: https://microbe.directory/developers.

## Outcomes/Findings

1. All kingdoms or microorganisms appear to have a correlation with animal pathogenicity, with the exception of viruses. Running a chi-square contingency table and testing significance of each kingdom, I see...
```
animal_pathogen  False  True 
kingdom                      
Archaea            171     57
Bacteria          1458   2391
Eukaryota           67     44
Viroids             41      0
Viruses           1676   1773

Power_divergenceResult(statistic=57.0, pvalue=4.3581190270320824e-14)
Power_divergenceResult(statistic=226.1597817614965, pvalue=4.1007210586066347e-51)
Power_divergenceResult(statistic=4.7657657657657655, pvalue=0.029031142135425358)
Power_divergenceResult(statistic=41.0, pvalue=1.5222921962563087e-10)
Power_divergenceResult(statistic=2.7280371122064366, pvalue=0.09860040143630405)
```