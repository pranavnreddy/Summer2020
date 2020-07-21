/* TODO:    - DONE implement quicksort, bubblesort, insertion sort 
            - DONE validate input
            - DONE? format HTML nicely
*/

function parseAndSort() {

    var input, text, choice;
    let mergeSortArr, quickSortArr, bubbleSortArr, insertionSortArr = [];

    input = document.getElementById("numb").value;

    try {
        input = input.split(',').map(function (element) {
            element = parseInt(element);
            if (isNaN(element)) {
                throw Error("Invalid input. Please try again.");
            }
            return element;
        });
    } catch (e) {
        document.getElementById("mergeSortArr").innerHTML = e.name + ": " + e.message;
        document.getElementById("quickSortArr").innerHTML = "";
        document.getElementById("bubbleSortArr").innerHTML = "";
        document.getElementById("insertionSortArr").innerHTML = "";
        return;
    }

    document.getElementById("preSortArr").innerHTML = "Before sorting: " + input;

    let presort = performance.now();
    mergeSortArr = mergeSort([...input]);
    let mergeTime = performance.now() - presort;

    presort = performance.now();
    quickSortArr = quickSort([...input]);
    let quickTime = performance.now() - presort;

    presort = performance.now();
    bubbleSortArr = bubbleSort([...input]);
    let bubbleTime = performance.now() - presort;

    presort = performance.now();
    insertionSortArr = insertionSort([...input]);
    let insertionTime = performance.now() - presort;

    document.getElementById("mergeSortArr").innerHTML = "Merge sort: " + mergeSortArr + "\nTime taken (ms): " + mergeTime;
    document.getElementById("quickSortArr").innerHTML = "Quick sort: " + quickSortArr + "\nTime taken (ms): " + quickTime;
    document.getElementById("bubbleSortArr").innerHTML = "Bubble sort: " + bubbleSortArr + "\nTime taken (ms): " + bubbleTime;
    document.getElementById("insertionSortArr").innerHTML = "Insertion sort: " + insertionSortArr + "\nTime taken (ms): " + insertionTime;
}

function randomSort() {
    const len = Math.floor(Math.random() * 10000 + 20);

    arr = [...Array(len)].map(() => Math.random() * 1000 - 500);

    document.getElementById("preSortArr").innerHTML = "# of elements: " + len +
        "<br>Largest #: " + Math.max(...arr) +
        "<br>Smallest #: " + Math.min(...arr);

    document.getElementById("mergeSortArr").innerHTML = "Sorting...";
    let presort = performance.now();
    mergeSortArr = mergeSort([...arr]);
    let mergeTime = performance.now() - presort;
    document.getElementById("mergeSortArr").innerHTML = "Merge sort took " + mergeTime + " milliseconds.";

    document.getElementById("quickSortArr").innerHTML = "Sorting...";
    presort = performance.now();
    quickSortArr = quickSort([...arr]);
    let quickTime = performance.now() - presort;
    document.getElementById("quickSortArr").innerHTML = "Quick sort took " + quickTime + " milliseconds.";

    document.getElementById("bubbleSortArr").innerHTML = "Sorting...";
    presort = performance.now();
    bubbleSortArr = bubbleSort([...arr]);
    let bubbleTime = performance.now() - presort;
    document.getElementById("bubbleSortArr").innerHTML = "Bubble sort took " + bubbleTime + " milliseconds.";

    document.getElementById("insertionSortArr").innerHTML = "Sorting...";
    presort = performance.now();
    insertionSortArr = insertionSort([...arr]);
    let insertionTime = performance.now() - presort;
    document.getElementById("insertionSortArr").innerHTML = "Insertion sort took " + insertionTime + " milliseconds.";
}

function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }

    const merge = (leftArr, rightArr) => {
        let mergedArr = [], leftIndex = 0, rightIndex = 0;

        while (leftIndex < leftArr.length && rightIndex < rightArr.length) {
            if (leftArr[leftIndex] < rightArr[rightIndex]) {
                mergedArr.push(leftArr[leftIndex]);
                leftIndex++;
            } else {
                mergedArr.push(rightArr[rightIndex]);
                rightIndex++;
            }
        }
        return mergedArr.concat(leftArr.slice(leftIndex)).concat(rightArr.slice(rightIndex));
    }

    let mid = Math.floor(arr.length / 2);
    let leftArr = arr.slice(0, mid);
    let rightArr = arr.slice(mid);

    return merge(mergeSort(leftArr), mergeSort(rightArr));
}

function quickSort(arr, startIndex = 0, finalIndex = arr.length) {
    const pivot = (pivotArr, pivotStart = 0, pivotFinal = arr.length + 1) => {
        const swap = (arr, a, b) => [arr[a], arr[b]] = [arr[b], arr[a]];
        let pivotValue = pivotArr[pivotFinal], pointer = pivotFinal;

        for (let i = pivotFinal; i >= pivotStart; i--) {
            if (arr[i] > pivotValue) {
                pointer--;
                swap(arr, pointer, i);
            }
        }
        swap(arr, pivotFinal, pointer);

        return pointer;
    }

    let pivotIndex = pivot(arr, startIndex, finalIndex);

    if (startIndex < finalIndex) {
        quickSort(arr, startIndex, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, finalIndex);
    }

    return arr.slice(0, arr.length - 1);
}

function bubbleSort(arr) {
    const swap = (arr, a, b) => [arr[a], arr[b]] = [arr[b], arr[a]];
    let len = arr.length;
    let hasSwapped;
    do {
        hasSwapped = false;
        for (let i = 0; i < len; i++) {
            if (arr[i] > arr[i + 1]) {
                swap(arr, i, i + 1)
                hasSwapped = true;
            }
        }
    } while (hasSwapped);
    return arr;
}

function insertionSort(arr) {
    let length = arr.length;
    for (let i = 1; i < length; i++) {
        let key = arr[i];
        let j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
    return arr;
}