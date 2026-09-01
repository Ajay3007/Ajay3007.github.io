#include<bits/stdc++.h>
using namespace std;

class Image {
private:
    unique_ptr<uint8_t[]> pixels; // Smart pointer to manage pixel data
    size_t width;
    size_t height;
public:
    Image(size_t w, size_t h) : width(w), height(h), pixels(make_unique<uint8_t[]>(w * h * 3)) {
        cout << "[Image] ctor: allocated " << static_cast<void*>(pixels.get()) << "\n";
    }
    // No destructor needed
    // No copy constructor 
    // No copy assignment
    // No move constructor
    // No move assignment
    // Compiler-generated ones are sufficient (Rule of 0)
    void fill(uint8_t r, uint8_t g, uint8_t b) {
        for (size_t i = 0; i < width * height * 3; i += 3) {
            pixels[i] = r;
            pixels[i + 1] = g;
            pixels[i + 2] = b;
        }
    }
    void printPixel(size_t x, size_t y) const {
        if (x >= width || y >= height) {
            cout << "Pixel out of bounds\n";
            return;
        }
        size_t index = (y * width + x) * 3;
        cout << "Pixel(" << x << ", " << y << "): ("
             << static_cast<int>(pixels[index]) << ", "
             << static_cast<int>(pixels[index + 1]) << ", "
             << static_cast<int>(pixels[index + 2]) << ")\n";
    }
};
int main() {
    Image img1(4, 4);
    img1.fill(255, 0, 0); // Fill with red color
    img1.printPixel(2, 2);

    cout << "\nDemonstrating move semantics automatically:\n";
    Image img2 = std::move(img1); // Uses compiler-generated move constructor

    cout << "After move:\n";
    cout << "img1 (moved-from):\n";
    cout << "Attempting to print pixel from moved-from img1:\n";
    cout << "Note: Accessing moved-from object is generally unsafe, but here we just demonstrate that pixels have been moved.\n";
    // img1.printPixel(2, 2); // pixels.get() is nullptr after move

    cout << "img2 (moved-to):\n";
    img2.printPixel(2, 2);

    return 0;
}