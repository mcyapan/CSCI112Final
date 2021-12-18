#!/usr/bin/env python3
import boto3

def create_table(
        ddb_table_name,
        partition_key,
        sort_key,
        GSIPK1,
        GSISK1,
        GSIPK2,
        GSISK2
        ):

#GSIPK1 and GSISK1 refers to the hash and range key for our global secondary index.
#GSIPK2 and GSISK2 refers to the hash and range key for our global secondary index.

    dynamodb = boto3.resource('dynamodb')

    table_name = ddb_table_name
    
    attribute_definitions = [
        {'AttributeName': partition_key, 'AttributeType': 'S'},
        {'AttributeName': sort_key, 'AttributeType': 'S'},
        {'AttributeName': GSIPK1, 'AttributeType': 'S'},
        {'AttributeName': GSISK1, 'AttributeType': 'N'},
        {'AttributeName': GSIPK2, 'AttributeType': 'S'},
        {'AttributeName': GSISK2, 'AttributeType': 'N'}
        ]
    
    key_schema = [{'AttributeName': partition_key, 'KeyType': 'HASH'}, 
                  {'AttributeName': sort_key, 'KeyType': 'RANGE'}]
                  
    provisioned_throughput = {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}
    
    gsi = [{
            'IndexName': 'Category_Index',
            'KeySchema': [
                {'AttributeName': GSIPK1, 'KeyType': 'HASH'},
                {'AttributeName': GSISK1, 'KeyType': 'RANGE'}],
            'Projection': { 'ProjectionType': 'ALL'},
            'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}
    },
    {
            'IndexName': 'Developer_Index',
            'KeySchema': [
                {'AttributeName': GSIPK2, 'KeyType': 'HASH'},
                {'AttributeName': GSISK2, 'KeyType': 'RANGE'}],
            'Projection': { 'ProjectionType': 'ALL'},
            'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 10}
    }]
    
    try:
        # Create a DynamoDB table with the parameters provided
        table = dynamodb.create_table(TableName=table_name,
                                      KeySchema=key_schema,
                                      AttributeDefinitions=attribute_definitions,
                                      ProvisionedThroughput=provisioned_throughput,
                                      GlobalSecondaryIndexes=gsi
                                      )
        return table
    except Exception as err:
        print("{0} Table could not be created".format(table_name))
        print("Error message {0}".format(err))

#The following function allows us to delete the table if needed.

def delete_table(name):
    dynamodb = boto3.resource('dynamodb')  
    table = dynamodb.Table(name)
    table.delete()

#The create_table function here is now called. We have two secondary indexes.
#The first index consists of a Category hash key and a Rating range key.
#The second index consists of a Developer hash key and an Installs range key.

if __name__ == '__main__':
    table = create_table("appstore", "PK", "SK", "Category", "Rating", "Developer", "Installs")
