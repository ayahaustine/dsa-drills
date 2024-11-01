/* I am trying to write a scoring system for bowling in C++.
I want the user to be able to enter their score for each roll
and then the output updates each time to display the users score in real time.
Account for things like strikes and spares and the 10th frame. Make sure the 
output is evenly spaced and looks clean and professional.

*/

// possible solution 1


#include <iostream>
#include <vector>
#include <iomanip>

const int MAX_FRAMES = 10;

class BowlingGame {
public:
    BowlingGame() : frames_(MAX_FRAMES), currentFrame_(0), currentRoll_(0) {}

    void roll(int pins) {
        if (currentFrame_ < MAX_FRAMES) {
            frames_[currentFrame_].push_back(pins);
            updateScore();
            if (currentRoll_ == 0) {
                // First roll of frame
                if (pins == 10) {
                    currentFrame_++; // Next frame for a strike
                } else {
                    currentRoll_++; // Move to second roll
                }
            } else {
                // Second roll of frame
                currentFrame_++;
                currentRoll_ = 0; // Reset rolls for the next frame
            }
        }
    }

    void displayScore() const {
        std::cout << "Frame\tRoll1\tRoll2\tScore\n";
        int totalScore = 0;
        for (int i = 0; i < MAX_FRAMES; ++i) {
            std::cout << i + 1 << "\t";
            if (frames_[i].size() > 0) {
                std::cout << frames_[i][0]; // First roll
            }
            std::cout << "\t";
            if (frames_[i].size() > 1) {
                std::cout << frames_[i][1]; // Second roll
            }
            std::cout << "\t" << totalScore + frameScore(i) << "\n";
            totalScore += frameScore(i);
        }
        std::cout << "Total Score: " << totalScore << std::endl;
    }

private:
    std::vector<std::vector<int>> frames_;
    int currentFrame_;
    int currentRoll_;

    int frameScore(int frameIndex) const {
        if (frameIndex >= MAX_FRAMES) return 0;

        int frameTotal = 0;
        if (frames_[frameIndex].size() > 0) {
            frameTotal += frames_[frameIndex][0]; // First roll
        }
        if (frames_[frameIndex].size() > 1) {
            frameTotal += frames_[frameIndex][1]; // Second roll
        }
        
        // Check for strikes and spares
        if (frameIndex < MAX_FRAMES - 1) { // Not last frame
            if (frames_[frameIndex][0] == 10) { // Strike
                if (frames_[frameIndex + 1].size() > 0) {
                    frameTotal += frames_[frameIndex + 1][0]; // Next frame's first roll
                    if (frames_[frameIndex + 1].size() > 1) {
                        frameTotal += frames_[frameIndex + 1][1]; // Next frame's second roll
                    } else if (frameIndex + 2 < MAX_FRAMES && frames_[frameIndex + 2].size() > 0) {
                        frameTotal += frames_[frameIndex + 2][0]; // Look for two rolls ahead
                    }
                }
            } else if (frameTotal == 10) { // Spare
                if (frameIndex + 1 < MAX_FRAMES && frames_[frameIndex + 1].size() > 0) {
                    frameTotal += frames_[frameIndex + 1][0]; // Next frame's first roll
                }
            }
        } else { // Last frame
            if (frameTotal >= 10 && frames_[frameIndex].size() > 2) {
                frameTotal += frames_[frameIndex][2]; // Bonus roll in the last frame
            }
        }

        return frameTotal;
    }

    void updateScore() {
        // This function can be extended to perform any additional operations after each roll
        displayScore(); // Display update after each roll
    }
};

int main() {
    BowlingGame game;
    int pins;

    for (int i = 0; i < 21; ++i) { // Maximum rolls
        if (i >= 20 && (i % 2 == 0)) { // During the 10th frame, allow for up to three rolls
            std::cout << "Enter pins knocked down (0-10 or double roll): ";
        } else {
            std::cout << "Enter pins knocked down (0-10): ";
        }
        
        std::cin >> pins;

        if (pins < 0 || pins > 10) {
            std::cout << "Invalid input. Please enter a number between 0 and 10." << std::endl;
            i--; // repeat this iteration
            continue;
        }
        
        game.roll(pins);
    }

    return 0;
}