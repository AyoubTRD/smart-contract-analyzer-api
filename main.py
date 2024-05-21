from lib.app import app

app.run(port=8000, debug=True)


# from lib.models.CNN_model import CNNModel

# I was testing BLSTM model
# from lib.models.BLSTM_model import BLSTMModel

# source_code = """
# pragma solidity ^0.4.15;
# contract Overflow {
#     uint private sellerBalance=0;
#     function add(uint value) returns (bool){
#         sellerBalance += value;
#     }
#     function safe_add(uint value) returns (bool){
#         require(value + sellerBalance >= sellerBalance);
#         sellerBalance += value;
#     }
# }
# """
# model = BLSTMModel()
# print(model.analyze(source_code))
