from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# wrap long words
@register.filter(name='word_wrap')
def word_wrap(word):
	words = word.split()
	if len(words) > 3:
		num_words = min(len(words), 6)  # 3 lines * 2 words per line = 6 words
		# Group words in pairs and limit to 3 lines
		paired_words = [' '.join(words[i:i + 3]) for i in range(0, num_words, 3)]
		# Join the pairs with <br> for HTML line breaks
		wrapped_word = '<br>'.join(paired_words)
		# Append '...' if there are more words than included
		if len(words) > num_words:
			wrapped_word += '...'
		# Mark the string as safe for HTML output
		return mark_safe(wrapped_word)
	else:
		return word

