/**
 * @param {number} big
 * @param {number} medium
 * @param {number} small
 */
var ParkingSystem = function (big, medium, small) {
    this.big = big;
    this.medium = medium;
    this.small = small;
};

/** 
 * @param {number} carType
 * @return {boolean}
 */
ParkingSystem.prototype.addCar = function (carType) {
    if (carType == 1) {
        var has = this.big > 0;
        if (has) {
            this.big--;
        }
        return has;
    } else if (carType == 2) {
        var has = this.medium > 0;
        if (has) {
            this.medium--;
        }
        return has;
    } else if (carType == 3) {
        var has = this.small > 0;
        if (has) {
            this.small--;
        }
        return has;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */

var parkingSystem = new ParkingSystem(1, 1, 0);
