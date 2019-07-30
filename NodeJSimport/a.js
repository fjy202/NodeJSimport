function enString(data){
    var key1 = "YHXWWLKJYXGS";
    var key2 = "ZFCHHYXFL10C";
    var key3 = "DES";
    var enchex = key1+key2+key3+data
    return enchex;
}
exports.e=enString