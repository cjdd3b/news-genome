# -*- coding: utf-8 -*- 
from timer import Timer
import math
from nltk import pos_tag,FreqDist,ConditionalFreqDist
from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize
from mlstripper import nohtml,timeme
from lib.SyllableCounter import CountSyllables
from news_genome import ArticleSource
import sys

@nohtml
@timeme
def word_count(text):
    return len(word_tokenize(text))

@nohtml
@timeme
def sentence_count(text):
    return len(sent_tokenize(text))

@nohtml
@timeme
def avg_sentence_length(text):
    sents = [len(word_tokenize(s)) for s in sent_tokenize(text)]
    return reduce(lambda x, y: x + y, sents) / float(len(sents))

@nohtml
@timeme
def avg_word_length(text):
    words = [len(w) for w in word_tokenize(text)]
    return reduce(lambda x, y: x + y, words) / float(len(words))

@nohtml
@timeme
def avg_word_syllables(text):
    words = [float(CountSyllables(w)) for w in word_tokenize(text)]
    return reduce(lambda x, y: x + y, words) / float(len(words))

@nohtml
@timeme
def flesch_readability(text):
    word_toks = word_tokenize(text)
    num_words = len(word_toks)
    num_syllables = sum([float(CountSyllables(w)) for w in word_toks])
    num_sentences = len(sent_tokenize(text))
    return 206.835 - (1.015 * (num_words / num_sentences)) - (84.6 * (num_syllables / num_words))

@nohtml
@timeme
def smog_readability(text):
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)
    polysyllables = sum(CountSyllables(x) > 3 for x in word_tokenize(text))
    return 1.0430 * math.sqrt(polysyllables * (30 / num_sentences)) + 3.1291

@timeme
def number_of_grafs(text):
    return len(regexp_tokenize(text, r'\<\/p\>', gaps=True))

@timeme
def avg_graf_length(text):
    grafs = [len(word_tokenize(p)) for p in regexp_tokenize(text, r'\<\/p\>', gaps=True)]
    return reduce(lambda x, y: x + y, grafs) / len(grafs)

@timeme
def length_of_first_graf(text):
    return word_count(regexp_tokenize(text, r'\<\/p\>', gaps=True)[0])

@nohtml
@timeme
def punct_count(text, punct='?'):
    return len(list(filter(lambda c: c in text, punct)))

@nohtml
@timeme
def pos_count(text,tag='NN'):
    words = word_tokenize(text)
    cfd = ConditionalFreqDist((tag,1) for word,tag in  pos_tag(words))
    return cfd[tag].N()

@nohtml
@timeme
def pos_percentages(text,tag='NN'):
    words = word_tokenize(text)
    cfd = ConditionalFreqDist((tag,1) for word,tag in  pos_tag(words))
    return float(cfd[tag].N())/float(len(words))

@timeme
def metrics(story):
    return [
         word_count(story),
         sentence_count(story),
         avg_word_length(story),
         number_of_grafs(story),
         length_of_first_graf(story),
         avg_sentence_length(story),
         avg_graf_length(story),
         punct_count(story, '?'),
         punct_count(story, '!'),
         punct_count(story, '"'),
         #pos_count(story,'NN'),
         #pos_count(story,'VBP'),
         #pos_count(story,'JJ'),
         pos_percentages(story,'NN'),
         pos_percentages(story,'VBP'),
         pos_percentages(story,'JJ'),
         avg_word_syllables(story),
         flesch_readability(story),
         smog_readability(story)                        
    ]

if __name__ == '__main__':
    # Cheap testing, one two

    story = '''
    <p>LOS ANGELES — Christopher J. Dorner had a long list of grievances and potential victims, most of them police officers he had once worked with, and he was already suspected of killing the daughter of a retired police official and her fianc&eacute;. So law enforcement officials moved rapidly to protect their own, removing officers from the streets and setting up the largest security detail in any city in recent history. </p> <p>“I’ve not seen anything like this in my time anywhere,” said William J. Bratton, a former police chief in Los Angeles and former police commissioner in New York. “The threats being made against families, the actual commission of murder, that is a line that is not crossed in America. The department had to create a plan of historic proportions.” </p> <p>Some 50 police department officials each had as many as eight plainclothes officers assigned to protect them and their families by patrolling their neighborhoods — an unprecedented level of protection for such a large group of officers. The focus meant that hundreds of officers were taken off regular duties, leaving some nonemergency calls to go unanswered. And the presence of plainclothes officers transformed life in dozens of suburban neighborhoods, as the police stood guard on porches with shotguns and used dogs to sniff for bombs in backyards. </p> <p>Most of the officers stayed off the street, forgoing their normal work to protect themselves. Some had their children stay home from school, and several went out of state. </p> <p>In all, as many as 500 officers — roughly 5 percent of the entire Los Angeles Police Department — spent the last week focusing on protecting one another from Mr. Dorner, a former police officer and Navy reservist. Law enforcement officials said Wednesday that they believed that Mr. Dorner died the day before as he barricaded himself in a cabin in the San Bernardino Mountains.</p> <p>“We believe the investigation is over at this point,” Sheriff John McMahon of San Bernardino County said at a news conference on Wednesday.</p> <p>Still, more than a dozen officers will remain under protection until the body is officially identified, a process that could take days, perhaps weeks. </p> <p>“We don’t just stop a murder case simply because we think the suspect in that case is no longer with us,” Lt. Andy Neiman of the Los Angeles police said Wednesday.</p> <p>Los Angeles officials would not comment on the details of the security force, for fear that it would compromise security. But interviews with several police officers, neighbors and crime experts suggest the vast scale of the undertaking and how seriously the city took the threats from Mr. Dorner, who was believed to be heavily armed. </p> <p>Mr. Dorner’s training and knowledge made the search even more complex, officials said. The police believe that Mr. Dorner, who was fired from the force in 2008, not only was listening to news media reports, but also would have known the right frequencies on the police radio.</p> <p>Patrol officers were pulled from regular duties like securing murder scenes, or from simply monitoring their regular areas, to provide extra officers for the security detail. In several cases, plainclothes officers were sent to crime scenes to protect the area because detectives in uniform feared being targets. The police believed that their marked cars would be targets themselves; Mr. Dorner is accused of shooting two Riverside police officers who were sitting at a red light last Thursday, as he continued to elude the authorities. One of the officers was killed, the other wounded.</p> <p>Hundreds of officers were put on overtime as they were asked to cover extra shifts. Officials say it is too early to measure the costs of the security precautions, but Mayor Antonio Villaraigosa estimated it would be around $2 million. </p> <p>“I told the chief to spare no expense,” Mr. Villaraigosa said in an interview Wednesday. Over the last week, the mayor spoke to nearly all of the officers who were under protection, and he said many of them felt “terrorized by this individual.”</p> <p>“Every one of us would put our body in front of our kids if we feared something would happen to them,” he said. “These people go into the line of fire every day, but they do not expect concrete danger for their families.”</p> <p>The department may have been forced to move officers from administrative desk jobs to the street, said Chuck Wexler, the executive director of the <a href="http://www.policeforum.org/">Police Executive Research Forum</a>. The practice is routine for visits by heads of state, for example, but is otherwise rare.</p> <p>“This is about as traumatic an event as you can think of for a police department, when you have a former police officer looking to kill other police officers,” Mr. Wexler said. “They’re going to put anyone they can on it — everyone is vulnerable.”</p> <p>While officers who focus on gangs and organized crime are often threatened, Mr. Bratton said, it is unusual for such threats to be carried out and rarer still for family members to be targeted. On Tuesday, Mr. Dorner seemed to make it clear that he was focusing on those connected to law enforcement; he apparently did not harm the maids who entered the apartment he had been hiding in near Big Bear Lake, or the man whose truck he stole while trying make his getaway. </p> <p>Last week, after the police concluded that Mr. Dorner seemed to be hunting officers, they began to flood the neighborhoods of the assumed targets. There were patrol cars at nearly every intersection of the Long Beach neighborhood of Theresa Evans, Mr. Dorner’s former supervising officer who disciplined him and whom he later accused of kicking a mentally ill suspect. </p> <p>“We were sitting here, and all of a sudden 11 squad cars showed up all over the area,” said Arthur Chadbourne, a neighbor. “They blocked off the whole area. They hit every cross street, every exit. We had no idea what was going on.”</p> <p>In some cases, neighbors did not even know they had a police officer living among them until the plainclothes security detail showed up, many of its members <a href="http://blogs.kcrw.com/whichwayla/2013/02/christopher-dorner-manhunt-hits-home">wielding shotguns</a>. While other law enforcement officials have said officers were understandably on edge, the Police Department has come under criticism for an episode last week in which officers shot two women in a pickup truck that they believed matched the description of Mr. Dorner’s vehicle. </p> <p>The tight security continued on Wednesday, even as the police believed Mr. Dorner had been killed the night before. At the funeral for Michael Crain, the Riverside Police officer Mr. Dorner is suspected of shooting last week, there were scores of police officers from as far away as San Diego and Las Vegas. </p>
    '''

    print word_count(story)
    print sentence_count(story)
    print avg_word_length(story)
    print number_of_grafs(story)
    print length_of_first_graf(story)
    print avg_sentence_length(story)
    print avg_graf_length(story)
    print punct_count(story, '?')
    print punct_count(story, '!')
    print punct_count(story, '”')
    print pos_count(story)
    print pos_percentages(story)
    print avg_word_syllables(story)
    print flesch_readability(story)
    print smog_readability(story) 
