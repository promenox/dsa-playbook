# --- compiler settings ---
CC = gcc
CFLAGS = -IC:/msys64/mingw64/include -Wall -Wextra -g
LDFLAGS = -LC:/msys64/mingw64/lib -lcunit

# --- files & directories ---
TARGET = build/test_cases.exe
SRC_DIR = src
TEST_DIR = tests
BUILD_DIR = build

# find all source files
SRC_FILES = $(wildcard $(SRC_DIR)/*.c) $(TEST_DIR)/test_cases.c
# replace .c with .o, put them in build/
OBJ_FILES = $(patsubst %.c, $(BUILD_DIR)/%.o, $(SRC_FILES))

# --- default rule ---
all: $(TARGET)

# --- link final executable ---
$(TARGET): $(OBJ_FILES) | $(BUILD_DIR)
	$(CC) $(OBJ_FILES) -o $@ $(LDFLAGS)

# --- compile each .c into a .o ---
$(BUILD_DIR)/%.o: %.c | $(BUILD_DIR)
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) -c $< -o $@

# --- ensure build directory exists ---
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# --- clean rule ---
.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)

# --- run rule ---
.PHONY: run
run: $(TARGET)
	./$(TARGET)