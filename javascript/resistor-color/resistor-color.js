let colorMap = new Map()
colorMap['black'] = 0;
colorMap['brown'] = 1;
colorMap['red'] = 2;
colorMap['orange'] = 3;
colorMap['yellow'] = 4;
colorMap['green'] = 5;
colorMap['blue'] = 6;
colorMap['violet'] = 7;
colorMap['grey'] = 8;
colorMap['white'] = 9;

// ColorCode returns the color code of a certain color
export const colorCode = (color) => {
	return colorMap[color];
};

//COLORS is an Array consisting of the keys of the colorMap
export const COLORS = Object.keys(colorMap)


// Alternative solution 1 - Why is this not workign?
//const COLORS = [...colorMap.keys()];

// Alternative solution 2 - This is not working either? Why?
//let keys = [];
//for (let key of colorMap.keys()) {
//	keys.push(key);
//}
//export const COLORS = keys

// Alternative solution 3 - This is not working either? hmm, why?
//export const COLORS = Array.from(colorMap.keys())
