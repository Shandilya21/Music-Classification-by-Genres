# Music Classification by Genres


Abstract. This project was primarily aimed to create an automated
system for classification model for music genres. The first step included
finding good features that demarcated genre boundaries clearly. A total
of five features, namely MFCC vector, chroma frequencies, spectral rolloff,
spectral centroid, zero-crossing rate were used for obtaining feature
vectors for the classifiers from the GTZAN genre dataset [5]. Many different
classifiers were trained and used to classify, each yielding varying
degrees of accuracy in prediction. An ensemble classifier based on majority
voting was then created to incorporate all of the classifiers into
one.

Key words: music, genre, classification, MFCC, GTZAN genre dataset


Data Sets:

We have used the GTZAN dataset from the MARYSAS website. This is the
dataset used in [5]. It contains 9 music genres, each genre has 100 audio clips
in .au format. The genres are - blues, classical, country, disco, pop, jazz, reggae,
rock, metal. Each audio clips has a length 30 seconds, are 22050Hz Mono 16-bit
files. The dataset incorporates samples from variety of sources like CDs, radios,
microphone recordings etc. We split the datset in 0.9 : 0.1 ratio and used 5-fold
cross validation for reporting the results.
  
  
Music genre classification is widely discussed in the MIR (Music Information Retrieval) Society and
 has been of interest for a variety of reasons, including management of large music collections.
The main purpose of this project was to implement few classification algorithms and compare their
 performance when applied to a practical problem. Specifically, we performed music genre
 classification of songs on a dataset containing 100 songs from 10 different genres.
