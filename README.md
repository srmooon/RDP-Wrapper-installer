# 🚀 RDP Wrapper Installer by SrMoon

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://microsoft.com/windows)
[![GUI](https://img.shields.io/badge/GUI-CustomTkinter-orange.svg)](https://github.com/TomSchimansky/CustomTkinter)

> **Instalador automático e inteligente para RDP Wrapper Library com interface gráfica moderna**

## 📋 Sobre o Projeto

O **RDP Wrapper Installer by SrMoon** é uma ferramenta completa e automatizada que simplifica drasticamente a instalação do RDP Wrapper Library no Windows. Com uma interface gráfica moderna e intuitiva, o instalador executa todos os passos necessários automaticamente, eliminando a complexidade manual do processo.

### 🎯 Características Principais

- ✅ **Interface Gráfica Moderna** - Built com CustomTkinter (tema dark)
- ✅ **Instalação Completamente Automatizada** - Zero intervenção manual
- ✅ **Detecção Inteligente de Desktop** - Suporte OneDrive e Desktop padrão
- ✅ **Execução Privilegiada** - Verificação e solicitação automática de admin
- ✅ **Logs Detalhados** - Acompanhe cada etapa em tempo real
- ✅ **Validação de Credenciais** - Interface intuitiva para usuário/senha
- ✅ **Download Automático** - RDP Plus e componentes necessários
- ✅ **Sequência Otimizada** - Ordem correta de instalação garantida

## 🔧 Funcionalidades

### 🎮 Interface Intuitiva
- **Tema Dark Moderno** com CustomTkinter
- **Validação em Tempo Real** de usuário e senha
- **Barra de Progresso** visual com status detalhado
- **Logs Coloridos** para fácil acompanhamento

### 🛠️ Processo de Instalação
1. **Configuração RDP** - Registry settings e serviços
2. **Criação de Usuário** - Usuário RDP com privilégios admin
3. **Download RDP Wrapper** - Versão mais recente do GitHub
4. **Execução Sequencial** - update.bat → install.bat → autoupdate.bat
5. **Configuração Final** - Atalhos e downloads complementares

### 📁 Arquivos Criados
- **Atalho RDPConf.exe** na área de trabalho
- **RemoteDesktopPlus.exe** baixado automaticamente
- **Usuário RDP** configurado e pronto para uso

## 🚀 Como Usar

### Pré-requisitos
- Windows 10/11
- Conexão com internet
- Privilégios de administrador

### Instalação
1. **Baixe** o executável mais recente da seção [Releases](../../releases)
2. **Execute** como administrador (obrigatório)
3. **Configure** usuário e senha na interface
4. **Clique** em "Start Installation"
5. **Aguarde** a conclusão automática
6. **Reinicie** quando solicitado

### Pós-Instalação
Após o reboot, use as credenciais configuradas para conectar via RDP:
- **Servidor:** `127.0.0.2`
- **Usuário:** [configurado por você]
- **Senha:** [configurada por você]

## 📸 Screenshots

### Interface Principal
![Interface](https://via.placeholder.com/600x400/2b2b2b/ffffff?text=Interface+Moderna+Dark+Theme)

### Processo de Instalação
![Instalação](https://via.placeholder.com/600x400/2b2b2b/ffffff?text=Logs+Detalhados+em+Tempo+Real)

## 🔍 Detalhes Técnicos

### Arquitetura
- **Linguagem:** Python 3.13
- **GUI Framework:** CustomTkinter
- **Empacotamento:** PyInstaller
- **Execução:** Single executable (.exe)

### Componentes Instalados
- **RDP Wrapper Library** v1.6.2 (oficial)
- **Autoupdate** v1.2 (comunidade)
- **RDP Configuration Tool** (RDPConf.exe)
- **Remote Desktop Plus** (cliente RDP avançado)

### Sequência de Execução
```bash
1. Registry Fix (ServiceDll)
2. update.bat (CMD admin)
3. install.bat (CMD admin) 
4. autoupdate.bat (CMD admin - 2x)
5. Shortcuts & Downloads
6. Reboot Request
```

## 🤝 Créditos

### Projeto Base
- **RDP Wrapper Library** - [Stas'M](https://github.com/stascorp/rdpwrap)
- **Autoupdate Script** - [asmtron](https://github.com/asmtron/rdpwrap)

### Ferramentas Utilizadas
- **CustomTkinter** - [TomSchimansky](https://github.com/TomSchimansky/CustomTkinter)
- **Remote Desktop Plus** - [donkz](https://www.donkz.nl/)

### Desenvolvido por
**SrMoon** - Automação e Interface Gráfica

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## ⚠️ Disclaimer

Este software é fornecido "como está", sem garantias. Use por sua própria conta e risco. O desenvolvedor não se responsabiliza por danos causados pelo uso desta ferramenta.

## 🔗 Links Úteis

- [RDP Wrapper Original](https://github.com/stascorp/rdpwrap)
- [Autoupdate Community](https://github.com/asmtron/rdpwrap)
- [Remote Desktop Plus](https://www.donkz.nl/download/remote-desktop-plus/)
- [CustomTkinter Docs](https://customtkinter.tomschimansky.com/)

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela! ⭐**

Made with ❤️ by [SrMoon](https://github.com/srmooon)

</div>
