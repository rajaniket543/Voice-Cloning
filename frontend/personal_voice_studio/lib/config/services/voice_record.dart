import 'dart:io';
import 'package:flutter/material.dart';
import 'package:record/record.dart';
import 'package:path_provider/path_provider.dart';
import '../services/api_service.dart';

class VoiceRecordScreen extends StatefulWidget {
  const VoiceRecordScreen({super.key});

  @override
  State<VoiceRecordScreen> createState() => _VoiceRecordScreenState();
}

class _VoiceRecordScreenState extends State<VoiceRecordScreen> {
  final Record recorder = Record();
  bool recording = false;
  String? filePath;

  Future<void> startRecording() async {
    if (await recorder.hasPermission()) {
      final dir = await getTemporaryDirectory();
      filePath = "${dir.path}/voice.wav";

      await recorder.start(
        path: filePath,
        encoder: AudioEncoder.wav,
        samplingRate: 24000,
      );

      setState(() => recording = true);
    }
  }

  Future<void> stopRecording() async {
    await recorder.stop();
    setState(() => recording = false);
  }

  Future<void> uploadVoice() async {
    if (filePath == null) return;
    final api = ApiService();
    await api.registerVoice(File(filePath!), "user_1");
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text("Voice uploaded")),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Record Voice")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: recording ? stopRecording : startRecording,
              child: Text(recording ? "Stop Recording" : "Start Recording"),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: uploadVoice,
              child: const Text("Upload Voice"),
            )
          ],
        ),
      ),
    );
  }
}
