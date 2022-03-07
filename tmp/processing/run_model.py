import pymysql, pymongo
import pandas as pd
import datetime as dt
import pyasrule as rule


def run():
    myclient = pymongo.MongoClient("mongodb://localhost:27018/")
    mydb = myclient["cocoa"]

    mydb.if_you_like.drop()
    my_like = mydb["if_you_like"]

    today = dt.date.today()
    one_week_ago = today - dt.timedelta(days=7)

    SQL_Query = query_transaction_data_last_week(one_week_ago)
    new_df = transform_to_tc_data_df(SQL_Query)
    tc_data_df = pd.read_csv('./tc_data_df.csv')
    tc_data_df['Transaction'] = tc_data_df['Transaction'].to_string()
    tc_data_df = tc_data_df.append(new_df)
    tc_data_df.to_csv('tc_data_df.csv', index=False)

    items = pd.read_csv('./tc_product.csv')
    items = list(items['product_name'])
    arule = rule.AssociationRules()
    arule.generateRules(transaction_df=tc_data_df, item_col="Item", transaction_id="Transaction")
    result = arule.market_basket_df

    metrics = ["Confidence", "Lift", "Cosine", "Jaccard", "Information_Gain"]
    features = ["Antecedent", "Consequent", "Support_Both", "Support_Antecedent", "Support_Consequent"]


    for item_name in items:
        if_you_like = dict()
        a = result.loc[result["Antecedent"] == item_name, :].sort_values(by="Jaccard", \
                                                                         ascending=False).head(5) \
            [features + ["Jaccard"]]
        product_map = get_product_map()
        product_id = product_map[item_name]
        if_you_like['product_id'] = product_id
        if_you_like['collaborative_filtering_list'] = [product_map[item] for item in list(a['Consequent'])]

        x = my_like.insert_one(if_you_like)


def query_transaction_data_last_week(week_ago):
    dbcon = pymysql.connect(host="127.0.0.1", port=3308, user="root", passwd="my-secret-pw", db='tc_store_new',
                            charset='utf8')
    SQL_Query = pd.read_sql_query(
        f'''SELECT transaction_id, product_name, quantity
            FROM tc_store_new.order o
                JOIN tc_store_new.product p
                    ON o.product_id = p.product_ID
                WHERE
                    o.created_on > '{week_ago}';''', dbcon)
    return SQL_Query


def get_product_map():
    dbcon = pymysql.connect(host="127.0.0.1", port=3308, user="root", passwd="my-secret-pw", db='tc_store_new',
                            charset='utf8')
    product_map_df = pd.read_sql_query(
        '''SELECT product_ID, product_name
                FROM tc_store_new.product''', dbcon)
    product_map = {row['product_name']: row['product_ID'] for index, row in product_map_df.iterrows()}
    return product_map


def transform_to_tc_data_df(SQL_Query):
    all_transaction = []
    for i, order in SQL_Query.iterrows():
        count = int(order['quantity'])
        each_order = (order['transaction_id'], order['product_name'])
        for qty in range(count):
            all_transaction.append(each_order)
    new_df = pd.DataFrame(all_transaction, columns=['Transaction', 'Item'])
    return new_df


if __name__ == '__main__':
    run()
