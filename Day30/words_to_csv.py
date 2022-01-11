import pandas

words ="och i att det som en på är för av med den till inte har de han om ett jag var men sig så vi hon från man kan när hade nu skulle år säger där också eller sin under efter ut ska vid mot då här bara mycket upp över vara alla kommer vad än andra finns får in sedan du få ha hur blir två vill hans många måste något mer detta utan sina går allt blev fick mig honom dem skall nya bli någon mellan även några första varit kronor sitt genom ta kom dag (Dag) fram Sverige kunde stora hela svenska procent ju göra ingen sa bra tre gör kanske oss själv bland annat gick redan se inom gå aldrig del väl åt henne kunna helt samma denna enligt fått olika stor tid vet lite gång både sätt ser miljoner hennes därför tidigare dock tror ur min dessa just ner flera varje hos gjorde tog gäller barn tar komma Stockholm igen står såg lika mest sade ändå ännu ja tycker tillbaka bättre innan nog ligger deras rätt ni människor alltid fall ger blivit ge fyra ny gamla annan eftersom trots kvar vilket säga tiden gjort vår ville"

list_words = words.split(' ')
data = {'swe': list_words}


data_frame = pandas.DataFrame(data)
data_frame.to_csv('swe_eng.csv')



