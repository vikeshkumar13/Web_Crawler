# importing pandas
import pandas as pd
# importing statistics
import statistics as st

# consider the lists
sepal_length = [51, 43, 24, 14, 15, 14, 16, 10, 4, 9]
sepal_width = [4, 5, 52, 46, 50, 44, 49]

# if length are not equal
if len(sepal_length) != len(sepal_width):
	# Append mean values to the list with smaller length
	if len(sepal_length) > len(sepal_width):
		mean_width = st.mean(sepal_width)
		sepal_width += (len(sepal_length)-len(sepal_width)) * [mean_width]
	elif len(sepal_length) < len(sepal_width):
		mean_length = st.mean(sepal_length)
		sepal_length += (len(sepal_width)-len(sepal_length)) * [mean_length]


# DataFrame with 2 columns
df = pd.DataFrame({'sepal_length(cm)': sepal_length,
				'sepal_width(cm)': sepal_width})
print(df)
