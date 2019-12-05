# Fine-Grained-Google-Search

Google Search is not enough. Sometimes we want to filter some results based on criteria, but Google doesn't give us the option. Then this repo was born to let you programmatically filter results. 

## Usage
```python
res_list=fine_grained_search(query, stop=300, func)
print(res_list
```

where `query` is the original query string, `func` is a function that takes url and filter it accordingly(you may invoke beautifulsoup or some other libs to achieve this)
