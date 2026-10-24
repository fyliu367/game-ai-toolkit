# Changelog

## 2026-10-24
- Updated "Arm Neural Super Sampling" to "Arm Neural Super Sampling + Frame Rate Upscaling" (Rendering & Tech Art). Added Neural Frame Rate Upscaling (NFRU), Arm's neural frame generation for mobile GPUs (up to 2× displayed frame rate). Plugin v1.1.0 adds NFRU to the UE 5.4 and 5.6 plugins, and Arm's 23 Sept 2026 post describes the open SDK and plugin. The cons now say that the figures are simulated or Arm's own with no independent tests yet, and that the NFRU model is still under active development under Arm's AI Model Community Licence. Added the GitHub plugin link. The efficiency figure is unchanged (vendor).
  - Primary: https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/introducing-neural-frame-rate-upscaling-in-arm-neural-graphics-sdk-for-game-engines-and-ue-plugins, https://github.com/arm/neural-graphics-for-unreal/releases, https://huggingface.co/Arm/neural-frame-rate-upscaling
  - Independent (the dev kit now provides NSS and NFRU, Mali G2-Ultra NX): https://www.unite.ai/arm-unveils-mali-g2-ultra-nx-its-first-ai-native-mobile-gpu/
- Updated "Stable Audio" to "Stable Audio 3.0" (Audio & Voice). The card described the older line. The 3.0 family was released on 20 May 2026 with four models: Small SFX, Small, Medium and Large. Small is on-device for clips up to 2 minutes, and Medium and Large reach about 6 minutes. Small SFX, Small and Medium have open weights, while Large is API or enterprise self-hosting only. Added inpainting and LoRA training. The licensed-data claim is attributed to Stability. Added the "Open" tag and the announcement link. No efficiency figure is published.
  - Primary: https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models
  - Independent (date, sizes, open vs API, lengths, $1M licence threshold): https://techcrunch.com/2026/05/20/stability-ai-release-a-new-audio-model-that-can-create-six-minute-songs/
- Updated "Cascadeur" to "Cascadeur (2026.2)" (Animation & Mocap). Version 2026.2 (6 Aug 2026) retrained AI inbetweening and Motion Generation on larger datasets and added animation layers (alpha), easing controls and BVH import. The MCP server for outside AI tools is marked as reported by CG Channel; it was not in my reading of the vendor post. Replaced the third-party price listing with CG Channel's figures: Indie $96/yr or $19/mo for earners under $100k, rent-to-own. Added a con that the free tier is not licensed for commercial use. Added the release link.
  - Primary: https://cascadeur.com/blog/view/cascadeur-2026-2-animation-layers-easing-new-languages
  - Independent (date, features, MCP server, pricing, free-tier licence): https://www.cgchannel.com/2026/08/nekki-releases-cascadeur-2026-2-with-animation-layers/
- Card count unchanged (89). No efficiency figures changed. All three releases predate the catalogue (13 Oct), but the cards had not reflected them.
- Checked and not changed: earlier updates are already in the open branches update/2026-10-16 to update/2026-10-23. I found no official Veo 4 or Runway Gen-5 release, and no open-weight Wan 3.0 release (reported as API-only). I also found no qualifying October news for Hunyuan3D, TRELLIS, SAM 3D, FLUX, Unity AI (still open beta), Unreal MCP, Audio2Face, XeSS, MetalFX, Snapdragon GSR, Move AI, Rokoko, modl.ai, nunu.ai or the localization tools. I left out Grimoire (ErudAite), which has single-source press coverage only.

## 2026-10-13
- Added official links to all 89 tool cards (each checked to load the right page).
- Initial catalogue: 12 disciplines, 89 tools.
- Fact-check pass: stage-level labels on studio figures, updated licence and legal status for Midjourney, Suno, VibeVoice, ACE-Step, Sora and AMD FSR, and removed one unsupported claim.
- Removed all projected estimates. Cards without a published figure now say "No published figure yet" (26 sourced figures, 63 not published).
- Removed named-studio references.
