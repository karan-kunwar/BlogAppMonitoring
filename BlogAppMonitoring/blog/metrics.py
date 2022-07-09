from prometheus_client import Counter, Histogram

custom_home_page_views = Counter('custom_home_page_views', 'No. of times a user visits home page')
custom_post_detail_views = Counter('custom_post_detail_views', 'No. of times a user open details of a post')
custom_network_lateny = Histogram('custom_network_lateny', 'desc')