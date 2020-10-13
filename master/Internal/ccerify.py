from cancerify.cancerify import *
args = CancerifierArgument({'use_emoji': True, 'max_emoji': 50, 'prettify': False, 'content': '''squeze me asshole'''})

print(Cancerifier.cancerify(args))

