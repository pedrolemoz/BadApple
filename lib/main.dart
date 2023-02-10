import 'dart:io';

import 'bad_apple.dart';

void main() {
  final duration = 128;
  for (final frame in frames) {
    stdout.nonBlocking.write("\t\033[H\033[J");
    sleep(Duration(milliseconds: duration));
    stdout.write(frame);
  }
}
