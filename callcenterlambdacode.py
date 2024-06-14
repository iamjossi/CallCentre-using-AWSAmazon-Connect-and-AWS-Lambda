import json
 
def lambda_handler(event, context):
    #print(event)
    orderNo = event['Details']['Parameters']['OrderNo'];
    print("OrderNo is: " + str(orderNo))
     
    # Your code to fetch Order Status from database etc.
    orderStatus = "Shipped"
    expectedDeliveryDate = "31st December 2022"
     
    resultMap = {
        "OrderStatus": orderStatus,
        "ExpectedDeliveryDate": expectedDeliveryDate
        }
    return resultMap
