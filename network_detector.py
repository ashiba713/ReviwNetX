import networkx as nx

def detect_review_networks(df):
    G = nx.Graph()

    for _, row in df.iterrows():
        user_node = f"user_{row['user']}"
        product_node = f"product_{row['product']}"
        G.add_edge(user_node, product_node)

    clusters = list(nx.connected_components(G))

    suspicious_users = set()
    for cluster in clusters:
        users = [n for n in cluster if n.startswith("user")]
        products = [n for n in cluster if n.startswith("product")]

        if len(users) >= 3 and len(products) >= 2:
            suspicious_users.update(users)

    return suspicious_users
