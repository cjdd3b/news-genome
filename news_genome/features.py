from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize

def word_count(text):
    return len(word_tokenize(text))

def sentence_count(text):
    return len(sent_tokenize(text))

def avg_sentence_length(text):
    sents = [len(word_tokenize(s)) for s in sent_tokenize(text)]
    return reduce(lambda x, y: x + y, sents) / len(sents)

def avg_word_length(text):
    words = [len(w) for w in word_tokenize(text)]
    return reduce(lambda x, y: x + y, words) / len(words)

def number_of_grafs(text):
    return len(regexp_tokenize(text, r'\<\\\/p\>', gaps=True))

def avg_graf_length(text):
    grafs = [len(word_tokenize(p)) for p in regexp_tokenize(text, r'\<\\\/p\>', gaps=True)]
    return reduce(lambda x, y: x + y, grafs) / len(grafs)

def length_of_first_graf(text):
    return word_count(regexp_tokenize(text, r'\<\\\/p\>', gaps=True)[0])

def punct_count(text, punct='?'):
    return len(list(filter(lambda c: c in text, punct)))


if __name__ == '__main__':
    # Cheap testing, one two

    story = '''
    "<p>Jennifer Medina reported from Los Angeles; Ian Lovett from Big Bear Lake, Calif.; and Fernanda Santos from Angelus Oaks, Calif. Erica Goode contributed reporting from Washington; Rebecca Fairley Raney from Riverside, Calif.; and Kitty Bennett from Tampa, Fla.<\/p>","bio_subject":"","body":"<p>LOS ANGELES \u2014 Christopher J. Dorner had a long list of grievances and potential victims, most of them police officers he had once worked with, and he was already suspected of killing the daughter of a retired police official and her fianc&eacute;. So law enforcement officials moved rapidly to protect their own, removing officers from the streets and setting up the largest security detail in any city in recent history. <\/p>\n<p>\u201cI\u2019ve not seen anything like this in my time anywhere,\u201d said William J. Bratton, a former police chief in Los Angeles and former police commissioner in New York. \u201cThe threats being made against families, the actual commission of murder, that is a line that is not crossed in America. The department had to create a plan of historic proportions.\u201d <\/p>\n<p>Some 50 police department officials each had as many as eight plainclothes officers assigned to protect them and their families by patrolling their neighborhoods \u2014 an unprecedented level of protection for such a large group of officers. The focus meant that hundreds of officers were taken off regular duties, leaving some nonemergency calls to go unanswered. And the presence of plainclothes officers transformed life in dozens of suburban neighborhoods, as the police stood guard on porches with shotguns and used dogs to sniff for bombs in backyards. <\/p>\n<p>Most of the officers stayed off the street, forgoing their normal work to protect themselves. Some had their children stay home from school, and several went out of state. <\/p>\n<p>In all, as many as 500 officers \u2014 roughly 5 percent of the entire Los Angeles Police Department \u2014 spent the last week focusing on protecting one another from Mr. Dorner, a former police officer and Navy reservist. Law enforcement officials said Wednesday that they believed that Mr. Dorner died the day before as he barricaded himself in a cabin in the San Bernardino Mountains.<\/p>\n<p>\u201cWe believe the investigation is over at this point,\u201d Sheriff John McMahon of San Bernardino County said at a news conference on Wednesday.<\/p>\n<p>Still, more than a dozen officers will remain under protection until the body is officially identified, a process that could take days, perhaps weeks. <\/p>\n<p>\u201cWe don\u2019t just stop a murder case simply because we think the suspect in that case is no longer with us,\u201d Lt. Andy Neiman of the Los Angeles police said Wednesday.<\/p>\n<p>Los Angeles officials would not comment on the details of the security force, for fear that it would compromise security. But interviews with several police officers, neighbors and crime experts suggest the vast scale of the undertaking and how seriously the city took the threats from Mr. Dorner, who was believed to be heavily armed. <\/p>\n<p>Mr. Dorner\u2019s training and knowledge made the search even more complex, officials said. The police believe that Mr. Dorner, who was fired from the force in 2008, not only was listening to news media reports, but also would have known the right frequencies on the police radio.<\/p>\n<p>Patrol officers were pulled from regular duties like securing murder scenes, or from simply monitoring their regular areas, to provide extra officers for the security detail. In several cases, plainclothes officers were sent to crime scenes to protect the area because detectives in uniform feared being targets. The police believed that their marked cars would be targets themselves; Mr. Dorner is accused of shooting two Riverside police officers who were sitting at a red light last Thursday, as he continued to elude the authorities. One of the officers was killed, the other wounded.<\/p>\n<p>Hundreds of officers were put on overtime as they were asked to cover extra shifts. Officials say it is too early to measure the costs of the security precautions, but Mayor Antonio Villaraigosa estimated it would be around $2 million. <\/p>\n<p>\u201cI told the chief to spare no expense,\u201d Mr. Villaraigosa said in an interview Wednesday. Over the last week, the mayor spoke to nearly all of the officers who were under protection, and he said many of them felt \u201cterrorized by this individual.\u201d<\/p>\n<p>\u201cEvery one of us would put our body in front of our kids if we feared something would happen to them,\u201d he said. \u201cThese people go into the line of fire every day, but they do not expect concrete danger for their families.\u201d<\/p>\n<p>The department may have been forced to move officers from administrative desk jobs to the street, said Chuck Wexler, the executive director of the <a href=\"http:\/\/www.policeforum.org\/\">Police Executive Research Forum<\/a>. The practice is routine for visits by heads of state, for example, but is otherwise rare.<\/p>\n<p>\u201cThis is about as traumatic an event as you can think of for a police department, when you have a former police officer looking to kill other police officers,\u201d Mr. Wexler said. \u201cThey\u2019re going to put anyone they can on it \u2014 everyone is vulnerable.\u201d<\/p>\n<p>While officers who focus on gangs and organized crime are often threatened, Mr. Bratton said, it is unusual for such threats to be carried out and rarer still for family members to be targeted. On Tuesday, Mr. Dorner seemed to make it clear that he was focusing on those connected to law enforcement; he apparently did not harm the maids who entered the apartment he had been hiding in near Big Bear Lake, or the man whose truck he stole while trying make his getaway. <\/p>\n<p>Last week, after the police concluded that Mr. Dorner seemed to be hunting officers, they began to flood the neighborhoods of the assumed targets. There were patrol cars at nearly every intersection of the Long Beach neighborhood of Theresa Evans, Mr. Dorner\u2019s former supervising officer who disciplined him and whom he later accused of kicking a mentally ill suspect. <\/p>\n<p>\u201cWe were sitting here, and all of a sudden 11 squad cars showed up all over the area,\u201d said Arthur Chadbourne, a neighbor. \u201cThey blocked off the whole area. They hit every cross street, every exit. We had no idea what was going on.\u201d<\/p>\n<p>In some cases, neighbors did not even know they had a police officer living among them until the plainclothes security detail showed up, many of its members <a href=\"http:\/\/blogs.kcrw.com\/whichwayla\/2013\/02\/christopher-dorner-manhunt-hits-home\">wielding shotguns<\/a>. While other law enforcement officials have said officers were understandably on edge, the Police Department has come under criticism for an episode last week in which officers shot two women in a pickup truck that they believed matched the description of Mr. Dorner\u2019s vehicle. <\/p>\n<p>The tight security continued on Wednesday, even as the police believed Mr. Dorner had been killed the night before. At the funeral for Michael Crain, the Riverside Police officer Mr. Dorner is suspected of shooting last week, there were scores of police officers from as far away as San Diego and Las Vegas. <\/p>"
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